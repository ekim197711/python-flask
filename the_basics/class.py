

class SpaceShip:
    gravity=0.7
    def __init__(self, name, crew, fuel):
        self.name = name
        self.crew = crew
        self.fuel = fuel

    def str(self):
        return "name {}, crew {}, fuel {} gravity {}".format(self.name,
                                            self.crew,
                                            self.fuel,
                                            self.gravity)

    def addcrewmember(self):
        self.crew = self.crew + 1

    @staticmethod
    def calcDistance(x, y, z):
        return x * y * z

    @classmethod
    def calcWeight(cls, weight):
        return cls.gravity * weight



SpaceShip.gravity=0.65
print("I would weigh {} on the spaceship".format(SpaceShip.calcWeight(105)))

print(SpaceShip.calcDistance(10,20,30))
ss1=SpaceShip("Eagle", 100, 99)

print(ss1.calcDistance(10,20,30))
SpaceShip.gravity=0.6
ss2=SpaceShip("Seagul", 12, 60)
ss2.lazers=15
ss2.addcrewmember()
print("Lazers aboard {}".format(ss2.lazers))

print(ss1.str())
print(ss2.str())
print(SpaceShip.str(ss2))

