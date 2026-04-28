
### **Autonomous BI Research Agent: A Framework for Traceable Agency**
**How do we safely transition from AI that talks to AI that acts**

### **What This Is**
At its core this is an engineering framework designed to solve the **Agency Drift** problem in enterprise AI. While standard chatbots provide static responses this project implements a **Multi Agent Orchestration** system that can navigate complex data environments while remaining 100 percent auditable and safe.

**This repository contains:**
* **The Orchestration Graph agent.py:** A state based reasoning engine built with **LangGraph** that manages autonomous planning and execution.
* **The Enterprise Data Context database.py:** A simulated business intelligence environment featuring SQL based performance and churn datasets.
* **Safety and Oversight Modules:** Implementation of the **Human in the Loop HITL** persistence pattern to prevent autonomous errors in high stakes business tasks.

### **To Run This Framework:**
```bash
git clone https://github.com/zindzigriffin/autonomous-bi-agent
cd autonomous-bi-agent
pip install -r requirements.txt
python database.py # Initializes the enterprise data environment
python agent.py    # Launches the agentic loop
```

### **Repository Structure**
```text
autonomous-bi-agent/
├── README.md
├── agent.py            ← The Brain LangGraph orchestration and logic
├── database.py         ← Mock enterprise SQL and CSV data generation
├── .env                ← API credentials OpenAI or Google
├── requirements.txt    ← Python dependencies
└── .devcontainer/      ← Cloud native configuration for GitHub Codespaces
```

---

### **Why This Project Exists**
In the move toward **Autonomous Agents** we are facing a critical safety gap: **The Black Box Problem.** When an AI is given the power to query databases and generate reports it often does so in a single thought leaving no room for human intervention or error correction until the work is already finished.

In an enterprise setting a mistake is not just a typo but a data integrity failure. If an AI agent misunderstands a business query or encounters a technical error it needs a way to self heal and more importantly a way to wait for human verification.

### **The Core Problem with Agentic Reliability**
When we deploy agents to handle business intelligence we make a dangerous assumption: that the agent plan is always aligned with the user intent. Without a structured workflow agents can:
1.  **Hallucinate Logic:** Taking an incorrect path to find a data point.
2.  **Fail Silently:** Crashing when a database link is broken instead of finding a workaround.
3.  **Act Without Permission:** Executing costly or sensitive data queries without oversight.

### **What This Project Does**
This project treats Agency as a process that must be managed not just a capability. I developed a **Controlled Agency Workflow** that forces the AI to act as a transparent partner rather than a black box.

* **Decompositional Planning:** The system uses a **Planner Node** to break vague business intents into verifiable sub tasks.
* **Self Healing Execution:** The framework monitors its own execution health. If a tool call fails a **Reviewer Node** routes the error back to the Planner for recursive correction.
* **Traceable Memory:** By using a structured StateGraph every decision the agent makes is stored in a persistent memory making its reasoning path fully auditable for enterprise compliance.

---

### **The Methodology: Human in the Loop HITL Safety**
The centerpiece of this framework is the **Persistence Based Interrupt.** I have implemented a mandatory Pause in the agent reasoning cycle:

1.  **Autonomous Proposal:** The agent analyzes the query and proposes a multi step investigation path.
2.  **The State Freeze:** Utilizing InMemorySaver the agent mathematical state is frozen in time.
3.  **Human Audit:** The system waits for a human to review the plan.
4.  **Resumed Action:** Only after explicit approval does the agent execute its plan ensuring the human remains the Final Boss of the decision making process.

### **The Practical Application: Predictive Enterprise Intelligence**
This framework is a proof of concept for **Safe Autonomous Analytics.** By applying these layers of oversight businesses can trust AI to handle complex research tasks like analyzing churn or revenue dips without fearing that the AI will drift away from the intended goal. 

---

### **Tech Stack**
* **Orchestration:** LangGraph State based logic
* **LLM:** OpenAI GPT 4 or Google Gemini 1.5 Pro
* **Data:** SQL SQLAlchemy and Pandas
* **Environment:** GitHub Codespaces Cloud Native

### **About the Researcher**
**Zindzi Griffin** is an applied ML engineer focused on making AI systems auditable and safe. This project reflects her core belief: that for AI to be truly useful in the enterprise it must be as predictable and controllable as the software it lives inside.
