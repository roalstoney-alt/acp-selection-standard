class Result:
    def __init__(self, success, latency):
        self.success = success
        self.latency = latency

    def to_dict(self):
        return {
            "success": self.success,
            "latency": self.latency
        }
