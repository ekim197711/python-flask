from flask import Flask, render_template, request, redirect, url_for

from SpaceShipForm import SpaceShipForm

used_spaceships_app = Flask('app')
used_spaceships_app.config['SECRET_KEY'] = 'sadfsaxcvcveafsdfsd'

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


@used_spaceships_app.route('/welcome')
def welcome():
    return render_template("welcome.html", mytitle='Welcome')


@used_spaceships_app.route('/spareparts')
def myspareparts():
    return render_template("spareparts.html",mytitle='Spareparts')


@used_spaceships_app.route('/deliverytime')
def current_deliverytime():
    return render_template("deliverytime.html", mytitle='Deliverytime')


@used_spaceships_app.route('/newspaceship', methods=['GET', 'POST'])
def newspaceship():
    form = SpaceShipForm()
    if (request.method == 'POST'):
        if (form.validate_on_submit() == True):
            spaceships.append(SpaceShip(form.name.data,
                                        form.crew.data,
                                        form.weight.data))
            return redirect( url_for('listtheships') )
        else:
            pass
    else:
        pass

    return render_template("newspaceship_template.html",
                           mytitle='Create Spaceship',
                           form=form)




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