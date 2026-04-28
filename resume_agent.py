from agent import graph # Import the graph you already built

# We must use the SAME thread_id to access the frozen memory
config = {"configurable": {"thread_id": "sap_demo_1"}}

print("--- MANAGER APPROVAL SYSTEM ---")
# 1. Fetch the current state from memory
current_state = graph.get_state(config)
print(f"Current Plan in Memory: {current_state.values['plan']}")

# 2. Ask the user for approval
approval = input("Do you approve this plan? (yes/no): ")

if approval.lower() == "yes":
    # 3. Resume the agent from where it left off
    print("Resuming agent...")
    for event in graph.stream(None, config, stream_mode="values"):
        # We pass 'None' because the inputs are already in memory
        print(f"Current Status: {event.get('status')}")
else:
    print("Plan rejected. Agent stopped.")