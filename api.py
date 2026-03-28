from protocols.task import Task
from protocols.trace import build_trace
from recorder import record_trace
from evaluator import update_agent_score
from allocator import allocate_agent
from storage import load_agents, save_agents

registry = {}

def register_agent(agent):
    registry[agent.agent_id] = agent

def run_task(task_type, payload=None):
    agents_state = load_agents()

    selected = allocate_agent(agents_state)
    agent = registry.get(selected["agent_id"])

    task = Task(task_type, payload)

    result = agent.run(task)

    trace = build_trace(agent.agent_id, task, result)
    record_trace(trace)

    updated = update_agent_score(agents_state, agent.agent_id, result.to_dict())
    save_agents(updated)

    return {
        "agent": agent.agent_id,
        "result": result.to_dict()
    }
