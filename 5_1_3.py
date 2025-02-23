class RedButton:
    def __init__(self):
        self.count_click = 0
    
    def click(self):
        print("Тревога!")
        self.count_click += 1
    
    def count(self):
        return self.count_click