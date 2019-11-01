from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class SpaceShipForm(FlaskForm):
    name = StringField("Name of Spaceship", validators=[DataRequired(), Length(min=5, max=25)])
    crew = IntegerField("Number of crewmember required", validators=[DataRequired(),
                                                                     NumberRange(min=10,max=1000)])
    weight = DecimalField("Weight on Earth", validators=[NumberRange(min=100, max=20000)])
    submit = SubmitField("Create the spaceship")

