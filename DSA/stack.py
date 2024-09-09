class stack:
    def __init__(self) -> None:
        self.container = []
    
    def push(self,value):
        self.container.insert(value)
    
    def top(self):
        return self.container[-1]

    def pop(self):
        self.container.pop()
