from flask import Flask, render_template

used_spaceships_app = Flask('app')

class SpaceShip:
    def __init__(self, name, crew, weight):
        self.name = name
        self.crew = crew
        self.weight = weight

spaceships=[
    SpaceShip('Eagle', 100, 700),
    SpaceShip('Round', 1002, 670),
    SpaceShip('Black Bird', 550, 1000),
    SpaceShip('Seagul', 13, 23400),
    SpaceShip('Pingvin', 200, 12300),
    SpaceShip('Austridge', 500, 11200)
]


@used_spaceships_app.route('/list')
def listtheships():
    return render_template("listtheships.html",
                           mytitle='Used spaceships',
                           ships=spaceships)


@used_spaceships_app.route('/shop')
def usedspaceships():
    return """
    <h1>Welcome to my used spaceship shop</h1> 
    <p>- Have a look around</p>
    """

if __name__ == '__main__':
    used_spaceships_app.run(host='0.0.0.0', port=8090, debug=True)