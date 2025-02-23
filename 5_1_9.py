class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []