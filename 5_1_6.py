class Rectangle:
    def __init__(self, f_ang, s_ang):
        self.f_x, self.f_y = f_ang[0], f_ang[1]
        self.s_x, self.s_y = s_ang[0], s_ang[1]
    
    def perimeter(self):
        return round(abs(self.f_x - self.s_x) * 2 + abs(self.f_y - self.s_y) * 2, 2)
    
    def area(self):
        return round(abs(self.f_x - self.s_x) * abs(self.f_y - self.s_y), 2)
    
    def get_pos(self):
        return (round(min(self.f_x, self.s_x), 2), round(max(self.s_y, self.f_y), 2))
        
    def get_size(self):
        return (round(abs(self.f_x - self.s_x), 2), round(abs(self.f_y - self.s_y), 2))
    
    def move(self, dx, dy):
        self.f_x += dx
        self.f_y += dy
        self.s_x += dx
        self.s_y += dy
    
    def resize(self, width, height):
        p_w = abs(self.f_x - self.s_x)
        p_h = abs(self.f_y - self.s_y)
        if self.f_x > self.s_x:
            self.f_x += width - p_w
        else:
            self.s_x += width - p_w
        
        if self.f_y < self.s_y:
            self.f_y -= height - p_h
        else:
            self.s_y -= height - p_h
