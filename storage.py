import json

AGENT_FILE = "data/agents.json"

def load_agents():
    try:
        with open(AGENT_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_agents(agents):
    with open(AGENT_FILE, "w") as f:
        json.dump(agents, f, indent=2)
