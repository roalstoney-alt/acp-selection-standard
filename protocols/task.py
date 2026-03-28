class Task:
    def __init__(self, task_type, payload=None):
        self.task_type = task_type
        self.payload = payload or {}
