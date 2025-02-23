class Programmer:
    def __init__(self, name, pos):
        self.name = name
        self.position = pos
        self.work_hours = 0
        self.need_pay = 0
        match self.position:
            case "Junior":
                self.payment = 10
            case "Middle":
                self.payment = 15
            case "Senior":
                self.payment = 20

    def work(self, time):
        self.work_hours += time
        self.need_pay += time * self.payment

    def info(self):
        return f"{self.name} {self.work_hours}ч. {self.need_pay}тгр."

    def rise(self):
        match self.position:
            case "Junior":
                self.position = "Middle"
                self.payment = 15
            case "Middle":
                self.position = "Senior"
                self.payment = 20
            case "Senior":
                self.payment += 1