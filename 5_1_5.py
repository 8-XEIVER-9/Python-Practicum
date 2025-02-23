class Rectangle:
    def __init__(self, f_ang, s_ang):
        self.f_x, self.f_y = f_ang[0], f_ang[1]
        self.s_x, self.s_y = s_ang[0], s_ang[1]
    
    def perimeter(self):
        return round(abs(self.f_x - self.s_x) * 2 + abs(self.f_y - self.s_y) * 2, 2)
    
    def area(self):
        return round(abs(self.f_x - self.s_x) * abs(self.f_y - self.s_y), 2)