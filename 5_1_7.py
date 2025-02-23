class Rectangle:
    def __init__(self, corner1, corner2):
        self.x = round(min(corner1[0], corner2[0]), 2)
        self.y = round(max(corner1[1], corner2[1]), 2)
        self.width = round(abs(corner1[0] - corner2[0]), 2)
        self.height = round(abs(corner1[1] - corner2[1]), 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return (self.x, self.y)

    def get_size(self):
        return (self.width, self.height)

    def move(self, dx, dy):
        self.x = round(self.x + dx, 2)
        self.y = round(self.y + dy, 2)

    def resize(self, new_width, new_height):
        self.width = round(new_width, 2)
        self.height = round(new_height, 2)

    def turn(self):
        old_width = self.width
        old_height = self.height
        self.width, self.height = old_height, old_width
        delta_x = round((old_width - self.width) / 2, 2)
        delta_y = round((old_height - self.height) / 2, 2)
        self.x += delta_x
        self.y -= delta_y

    def scale(self, ratio):
        new_width = round(self.width * ratio, 2)
        new_height = round(self.height * ratio, 2)
        delta_x = round((new_width - self.width) / 2, 2)
        delta_y = round((new_height - self.height) / 2, 2)
        self.x -= delta_x
        self.y += delta_y
        self.width = new_width
        self.height = new_height