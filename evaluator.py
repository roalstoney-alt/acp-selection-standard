def evaluate_trace(trace):
    if trace["success"]:
        return 1 / trace["latency"]
    return 0


def update_agent_score(agents, agent_id, result):
    DECAY = 0.9  # 

    #  
    avg_success = sum(a["success_rate"] for a in agents) / len(agents)

    for agent in agents:
        if agent["agent_id"] == agent_id:

            #  
            agent["success_rate"] *= DECAY
            agent["avg_latency"] *= DECAY

            agent["task_count"] += 1

            #  
            agent["success_rate"] += (1 - DECAY) * int(result["success"])
            agent["avg_latency"] += (1 - DECAY) * result["latency"]

            #  
            relative_perf = agent["success_rate"] - avg_success

            agent["score"] = (
                0.6 * relative_perf +
                0.4 * (1 / agent["avg_latency"])
            )

    return agents
