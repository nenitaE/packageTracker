from flask_wtf import FlaskForm
from wtforms.fields import (SelectField, BooleanField, StringField, SubmitField)
from wtforms.validators import DataRequired
from map.map import map

class ShippingForm(FlaskForm):
    sender_name = StringField("Sender_name", validators=[DataRequired()])
    recipient_name = StringField("Recipient_name", validators=[DataRequired()])
    origin = SelectField("Origin", validators=[DataRequired()], choices = [(k, k) for k in map.keys()])
    destination = SelectField("Destination", validators=[DataRequired()], 
        choices = [(k, k) for k in map.keys()])
    express_bool = BooleanField("Express_bool")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
