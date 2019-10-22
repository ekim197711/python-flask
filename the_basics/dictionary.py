
spaceship={"name": "Falcon", "crew": 123, "lazers": 10, "cargo": "minerals" }
print(spaceship)

def showOffSpaceship(name, crew, cargo, lazers):
    print("showing off the ship name {}, crew {}, cargo {}, lazers {}".format(
        name, crew, cargo, lazers
    ))

showOffSpaceship(**spaceship)
showOffSpaceship(spaceship["name"],
                 spaceship["crew"],
                 spaceship["cargo"],
                 spaceship["lazers"]
                 )

for k, v in spaceship.items():
    print("key {}, value {}".format(k, v))