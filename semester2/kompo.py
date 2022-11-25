class Elkomp:
    def __init__(self):
        pass

class Modstand(Elkomp):
    def __init__(self, ohm):
        super().__init__()
        self.ohm = ohm
    def __add__(self, r):
        a = Modstand(self.ohm + r.getValue())
        return a
    def getValue(self):
        return self.ohm

class Kondensator(Elkomp):
    def __init__(self, kapacitet):
        super().__init__()
        self.kapacitet = kapacitet

class Spole(Elkomp):
    def __init__(self, induktion):
        super().__init__()
        self.induktion = induktion
    def __str__(self):
        return "induktion: %s" % (self.induktion)

a = Spole(10)

print(a)

r1 = Modstand(200)
r2 = Modstand(250)
r3 = r1+r2
print(r3.getValue())
