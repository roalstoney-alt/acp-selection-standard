import random, time
from protocols.result import Result

class LocalAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def run(self, task):
        success = random.random() > 0.3
        latency = random.uniform(1.0, 2.0)
        return Result(success, latency)
