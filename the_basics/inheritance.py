
class Creature:
    def __init__(self, weight, height, **kv):
        print("Init Creature")
        self.weight = weight
        self.height = height


class Alien:
    def __init__(self, age, **kv):
        print("Init Alien")
        self.age = age

class Humanoid(Alien, Creature):
    def __init__(self, age, weight, height):
        print("Init Humaniod")
        # super().__init__(age=age, weight=weight, height=height)
        Creature.__init__(self, weight, height)
        Alien.__init__(self, age)

    def __repr__(self):
        return "weight: {} height: {} age: {}".format(
           self.weight,
           self.height,
           self.age)
# alien = Alien(55, 80, 3.05)

humanoid = Humanoid(65, 200, 5)
print(repr(humanoid))