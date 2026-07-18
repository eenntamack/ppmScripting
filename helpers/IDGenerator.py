class IDGenerator:
    def __init__(self):
        self.num = 0

    def create(self,cls):
        self.num += 1
        return f"{cls.__name__}_{self.num}"