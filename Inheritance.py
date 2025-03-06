class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    def __init__(self, name):
        super().__init__(name)
        self.test = 1
    def __getn__(self):
        return self.name

professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"
print(professor_mouse.__getn__())