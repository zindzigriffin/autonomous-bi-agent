import pandas as pd
import sqlite3
from typing import Annotated, List, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class AgentState(TypedDict):
    query: str
    plan: List[str]
    observations: List[str]
    status: str
    needs_correction: bool # New state variable

def planner(state: AgentState):
    print("\n--- PHASE 1: PLANNING ---")
    if state.get("needs_correction"):
        todo = ["Deep dive into APAC region to compare benchmarks"]
    else:
        todo = ["Query SQL database for revenue", "Analyze churn"]
    return {"plan": todo, "status": "waiting_for_approval", "needs_correction": False}

def human_review(state: AgentState):
    return state

def executor(state: AgentState):
    print("\n--- PHASE 3: EXECUTION ---")
    conn = sqlite3.connect("enterprise.db")
    df = pd.read_sql_query("SELECT * FROM performance WHERE region = 'North America'", conn)
    conn.close()
    
    rev_q3 = df['q3_revenue'].values[0]
    rev_q4 = df['q4_revenue'].values[0]
    result = f"Q3: {rev_q3}, Q4: {rev_q4}"
    
    return {"observations": [result], "status": "checking_results"}

# THE SELF-CORRECTION NODE
def reviewer(state: AgentState):
    print("\n--- PHASE 4: SELF-CORRECTION REVIEW ---")
    data = state["observations"][0]
    # Logic: If revenue dropped more than 10%, trigger a correction loop
    if "450000" in data: # Simulated check for the dip we know exists
        print("ALERT: Significant revenue dip detected. Triggering re-planning.")
        return {"needs_correction": True, "status": "re-routing"}
    return {"needs_correction": False, "status": "verified"}

# --- Graph Assembly ---
builder = StateGraph(AgentState)
builder.add_node("planner", planner)
builder.add_node("human_review", human_review)
builder.add_node("executor", executor)
builder.add_node("reviewer", reviewer)

builder.add_edge(START, "planner")
builder.add_edge("planner", "human_review")
builder.add_edge("human_review", "executor")
builder.add_edge("executor", "reviewer")

# Conditional Logic: If needs_correction is True, go back to planner. Else, END.
builder.add_conditional_edges(
    "reviewer",
    lambda x: "planner" if x["needs_correction"] else END
)

memory = MemorySaver()
graph = builder.compile(checkpointer=memory, interrupt_before=["human_review"])
if __name__ == "__main__":
    config = {"configurable": {"thread_id": "sap_demo"}}
    # We use a variable for the query to keep it clean
    initial_input = {"query": "Explain revenue drops", "needs_correction": False}

    print("Starting Agent...")
    
    # 1. First Run: Goes to the Interrupt
    for event in graph.stream(initial_input, config):
        print(event)

    print("\n--- MANUAL INTERVENTION REQUIRED ---")
    snapshot = graph.get_state(config)
    print(f"Proposed Plan: {snapshot.values.get('plan')}")
    
    user_input = input("Type 'yes' to approve the plan and execute: ")

    if user_input.lower() == "yes":
        print("\nResuming Execution...")
        # 2. Second Run: Resumes, hits Reviewer, and potentially Loops back to Planner
        for event in graph.stream(None, config):
            print(event)
    else:
        print("Execution cancelled by user.")