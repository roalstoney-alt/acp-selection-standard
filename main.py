import argparse
from recorder import record_trace
from evaluator import evaluate_trace, update_agent_score
from allocator import allocate_agent
from storage import load_agents, save_agents

def run_task(task_type):
    agents = load_agents()

    if not agents:
        print(" No agents found.")
        return

    selected = allocate_agent(agents)

    print(f"\n[ALLOCATE] Selected agent: {selected['agent_id']}")

    #  agent
    result = {
        import random

#  
import random

total_runs = sum([a["task_count"] for a in agents])

#  
import random

total_runs = sum([a["task_count"] for a in agents])

#  
if total_runs < 20:
    phase = "A_strong"
else:
    phase = "B_strong"

#  
if phase == "A_strong":
    if selected["agent_id"] == "agent_A":
        success = True
        latency = 1.5
    else:
        success = False
        latency = 2.5

else:  # B_strong
    if selected["agent_id"] == "agent_B":
        success = True
        latency = 1.4
    else:
        success = False   #  A
        latency = 2.5

result = {
    "success": success,
    "latency": latency
}

result = {
    "success": success,
    "latency": latency
}
    }

    trace = record_trace(selected["agent_id"], task_type, result)

    score = evaluate_trace(trace)

    updated_agents = update_agent_score(agents, selected["agent_id"], result)

    save_agents(updated_agents)

    print(f"[RESULT] success={result['success']} latency={result['latency']}")
    print("[TRACE RECORDED]")
    print("[SCORE UPDATED]\n")


def show_agents():
    agents = load_agents()

    print("\n=== Agent Status ===")
    for a in agents:
        print(a)
    print("====================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    #  command  run
    parser.add_argument(
        "command",
        nargs="?",
        default="run",
        choices=["run", "list"]
    )

    parser.add_argument("--task", default="demo_task")

    args = parser.parse_args()

    if args.command == "run":
        run_task(args.task)
    elif args.command == "list":
        show_agents()