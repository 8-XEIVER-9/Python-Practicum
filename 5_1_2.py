class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self, sec_p):
        return round((abs(self.x - sec_p.x)**2 + abs(self.y - sec_p.y)**2)**0.5, 2)
