import json
import time
import uuid

TRACE_FILE = "data/traces.json"

def record_trace(agent_id, task_type, result):
    trace = {
        "trace_id": str(uuid.uuid4()),
        "agent_id": agent_id,
        "task_type": task_type,
        "success": result["success"],
        "latency": result["latency"],
        "timestamp": time.time()
    }

    try:
        with open(TRACE_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(trace)

    with open(TRACE_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return trace
