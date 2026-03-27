import json
import hashlib
import time
from datetime import datetime

LOG_FILE = "acp_log.json"

def hash_record(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def load_previous():
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
            return logs[-1]["hash"]
    except:
        return None

def record(action, input_data, output_data, metrics):
    prev = load_previous()

    snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "input": input_data,
        "output": output_data,
        "metrics": metrics,
        "previous": prev
    }

    snapshot["hash"] = hash_record(snapshot)

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(snapshot)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print("Recorded:", snapshot["hash"])
    return snapshot