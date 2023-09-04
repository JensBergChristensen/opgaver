class Motor:
    def __init__(self, motortype, direction=0, rpm=0):
        print("Inittializing ", motortype)
        self.motortype = motortype
        self.direction = direction
        self.rpm = rpm
    def runMotor(self, direction, rpm):
        self.direction = direction
        self.rpm = rpm
        print("Running the motor in direction", self.direction,"with", self.rpm, "rpm")

class Person:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname
        self.ownmotor = []

    def addMotor (self, motor):
        try:
            print("Adding", motor.motortype, "to", self.name, "ownership")
            self.ownmotor.append(motor)
        except AttributeError as e:
            print("Tried to add", motor, "to persons motor ownership, but encountred error:", e)

servomotor = Motor("Servo")
servomotor.runMotor(1,200)
megamotor = Motor("megamotor")

p1 = Person("Jens", "Christensen")

p1.addMotor(5)
p1.addMotor(megamotor)
