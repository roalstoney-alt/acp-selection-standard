def allocate_agent(agents):
    #  agent 
    for agent in agents:
        if agent["task_count"] < 5:
            return agent

    # 
    import random
    if random.random() < 0.9:
        return sorted(agents, key=lambda x: x["score"], reverse=True)[0]

    return random.choice(agents)