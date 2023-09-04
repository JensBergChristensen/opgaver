class Widget:
    def __init__(self):
        self.msg = "Hello, I'm a widget!"
        self.index = index
    def replace(self):
        index = self.index("w")
        self.msg[index] = 'g'
    def __str__(self):
        return "My string is: " + self.msg

a = Widget()
a.replace()
print(a)
