import json
import os

TRACE_FILE = "data/traces.json"


def record_trace(trace):
    # 
    if not os.path.exists(TRACE_FILE):
        with open(TRACE_FILE, "w") as f:
            json.dump([], f)

    # 
    with open(TRACE_FILE, "r") as f:
        data = json.load(f)

    #  trace
    data.append(trace)

    # 
    with open(TRACE_FILE, "w") as f:
        json.dump(data, f, indent=2)