import argparse
from api import run_task, register_agent
from agents.local_agent import LocalAgent
from storage import load_agents


register_agent(LocalAgent("agent_A"))
register_agent(LocalAgent("agent_B"))


def run():
    res = run_task("demo_task")
    print(res)


def show():
    print(load_agents())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="run")

    args = parser.parse_args()

    if args.command == "run":
        run()
    elif args.command == "list":
        show()