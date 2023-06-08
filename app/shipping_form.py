from flask_wtf import FlaskForm
from wtforms.fields import (SelectField, BooleanField, StringField, SubmitField)
from wtforms.validators import DataRequired
from map.map import map

class ShippingForm(FlaskForm):
    origin = SelectField("Origin:", validators=[DataRequired()], choices = [(k, k) for k in map.keys()])
    destination = SelectField("Destination:", validators=[DataRequired()], choices = [(k, k) for k in map.keys()])
    sender_name = StringField("From:", validators=[DataRequired()])
    recipient_name = StringField("To:", validators=[DataRequired()])
    express_bool = BooleanField("Express?")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
