import time

def build_trace(agent_id, task, result):
    return {
        "agent_id": agent_id,
        "task": task.task_type,
        "success": result.success,
        "latency": result.latency,
        "timestamp": int(time.time())
    }
