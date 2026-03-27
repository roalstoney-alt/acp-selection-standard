Version: v0.1 (Adaptive Selection Prototype)
Added
Behavior recording (recorder.py)
Dynamic scoring system (evaluator.py)
Allocation engine with exploration (allocator.py)
Updated
main.py
Introduced environment phase switching
Added deterministic behavior for testing:
Phase 1: Agent A dominant
Phase 2: Agent B dominant
Ensured environment affects all agents (not just selected)
evaluator.py
Introduced adaptive scoring
Combined:
instant feedback
historical signal
allocator.py
Added exploration mechanism
Prevents early lock-in
Key Fixes
Fixed path dependence issue
Fixed no exploration deadlock
Fixed environment not observable problem
Result

System now supports:

Adaptive trust reallocation based on behavior change