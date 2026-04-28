# Autonomous BI Research Agent A Framework for Traceable Agency
**How do we safely transition from AI that talks to AI that acts**

### **What This Is**
At its core this is an engineering framework designed to solve the Agency Drift problem in enterprise AI. While standard chatbots provide static responses this project implements a Multi Agent Orchestration system that can navigate complex data environments while remaining 100 percent auditable and safe.

**This repository contains:**
* The Orchestration Graph agent.py: A state based reasoning engine built with LangGraph that manages autonomous planning execution and self correction.
* The Enterprise Data Context database.py: A simulated business intelligence environment featuring Synthetically Generated performance and churn datasets.
* Safety and Oversight Modules: Implementation of the Human in the Loop HITL persistence pattern to prevent autonomous errors in high stakes business tasks.

### **To Run This Framework**
```bash
git clone https://github.com/zindzigriffin/autonomous-bi-agent
cd autonomous-bi-agent
pip install -r requirements.txt
python database.py 
python agent.py
```

### **Repository Structure**
```text
autonomous-bi-agent/
├── README.md
├── agent.py            
├── database.py         
├── .env                
├── requirements.txt    
└── .devcontainer/
```

### **Why This Project Exists**
In the move toward Autonomous Agents we are facing a critical safety gap: The Black Box Problem. When an AI is given the power to query databases and generate reports it often does so in a single thought leaving no room for human intervention or error correction until the work is already finished.

In an enterprise setting a mistake is not just a typo but a data integrity failure. If an AI agent misunderstands a business query or encounters a technical error it needs a way to self heal and more importantly a way to wait for human verification.

### **The Core Problem with Agentic Reliability**
When we deploy agents to handle business intelligence we make a dangerous assumption: that the agent plan is always aligned with the user intent. Without a structured workflow agents can:
1.  Hallucinate Logic: Taking an incorrect path to find a data point.
2.  Fail Silently: Crashing when a database link is broken instead of finding a workaround.
3.  Act Without Permission: Executing costly or sensitive data queries without oversight.

### **What This Project Does**
This project treats Agency as a process that must be managed not just a capability. I developed a Controlled Agency Workflow that forces the AI to act as a transparent partner rather than a black box.

* Decompositional Planning: The system uses a Planner Node to break vague business intents into verifiable sub tasks.
* Recursive Self Correction: The framework monitors its own outputs. If the Reviewer Node identifies a significant data anomaly such as a revenue dip it triggers a Strategic Re route back to the planner to initiate a deep dive investigation.
* Traceable Memory: By using a structured StateGraph every decision the agent makes is stored in a persistent memory making its reasoning path fully auditable for enterprise compliance.

### **The Methodology Human in the Loop HITL Safety**
The centerpiece of this framework is the Persistence Based Interrupt. I have implemented a mandatory Pause in the agent reasoning cycle:

1.  Autonomous Proposal: The agent analyzes the query and proposes a multi step investigation path.
2.  The State Freeze: Utilizing InMemorySaver the agent mathematical state is frozen in time.
3.  Human Audit: The system waits for a human to review the plan.
4.  Resumed Action: Only after explicit approval does the agent execute its plan ensuring the human remains the Final Boss of the decision making process.

### **The Practical Application Synthetic Enterprise Intelligence**
This framework serves as a proof of concept for Safe Autonomous Analytics. All research is conducted against a Synthetically Generated Dataset designed to mirror real world business metrics. By using synthetic data we can benchmark agent performance against known ground truth anomalies ensuring that the self healing logic triggers reliably when it encounters a business risk.

### **Tech Stack**
* Orchestration: LangGraph State based logic
* Data Handling: SQL SQLAlchemy and Pandas
* Environment: GitHub Codespaces Cloud Native

### **What is Next**
The current framework establishes the core Safety and Re routing logic. Future iterations of this research will focus on:
* Dynamic Tool Selection: Allowing the agent to autonomously choose between SQL Python or External API tools based on the complexity of the query.
* Mechanistic Interpretability Integration: Implementing latent space monitoring to detect when an agent internal reasoning is drifting toward an unsafe or hallucinated state before it reaches the execution phase.
* Multi Source Verification: Expanding the data environment to include cross functional data silos to test the agent ability to resolve conflicting data points.

### **About the Researcher**
Zindzi Griffin is an applied ML engineer focused on making AI systems auditable and safe. This project reflects her core belief: that for AI to be truly useful in the enterprise it must be as predictable and controllable as the software it lives inside.
