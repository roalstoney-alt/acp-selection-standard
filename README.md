We don’t decide which agent is best.
We build systems that continuously discover it.



ACP Selection Standard (Prototype)
Overview
This project demonstrates a minimal behavior → trust → allocation system for AI agents.
It validates a key hypothesis:
Agent trust should be dynamic, not static. And allocation should adapt as agents improve or degrade.

🔁 Core Loop

Behavior → Evaluation → Score → Allocation → Feedback → (repeat)


⚙️ System Components
Module	Function
recorder	Capture agent execution results
evaluator	Convert behavior into score
allocator	Select agent based on score
storage	Persist agent state
🧪 Experiment Goal
We simulate a changing environment:
* Phase 1: Agent A is better
* Phase 2: Agent B becomes better
We verify whether the system can:
❗ Detect the change and switch to the new best agent

🔥 Key Result
After running the system:
* Agent A initially dominates
* Environment changes
* Agent B becomes better
* System switches to Agent B automatically

🧠 Key Insight
A system must not only find the best agent, but also update who is best over time.

🚨 Why This Matters
Most systems:
* Lock into early winners
* Cannot adapt to change
* Overweight historical performance
This system shows:
Trust can be continuously recalibrated based on behavior

🏗️ Architecture

acp-selection-standard/
├── main.py
├── recorder.py
├── evaluator.py
├── allocator.py
├── storage.py
└── data/


▶️ How to Run

python3 main.py

Run multiple times:

for i in {1..100}; do python3 main.py; done

Check results:

python3 main.py list


🔬 Experiment Design
Phase Logic

Phase 1 (early):
- A succeeds
- B fails

Phase 2 (later):
- A fails
- B succeeds


🧠 Core Mechanisms
1. Dynamic Scoring
Score is updated continuously based on:
* success
* latency
* recent performance

2. Exploration
System occasionally tries non-optimal agents:

20% random selection


3. Adaptation
System reacts to:
* performance drop
* new better agents

🔥 Key Achievement
✅ System successfully performs decision switching

🚀 Next Steps
* Real API agents (instead of simulation)
* Multi-agent competition
* Multi-task scoring
* Tool-level trust
* Web dashboard
