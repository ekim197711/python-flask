
class Alien:
    def __init__(self, race, height):
        self.race = race
        self.height = height;

    def __repr__(self):
        return "race: {}, height: {}".format(self.race, self.height)

    def __str__(self):
        return "We have a nice alien which is {}.\n Its {} meters tall!!!".format(self.race, self.height)

    def __len__(self):
        return len(self.race)

alien=Alien("harry", 3)
alien2=Alien("Small and slimy", 1)
alien3=Alien("Rock like", 30)
for a in [alien, alien2, alien3]:
    print(a)
    print(len(a))