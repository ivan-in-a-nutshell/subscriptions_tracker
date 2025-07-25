from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class SubscriptionForm(FlaskForm):
    name = StringField('Service Name', validators=[DataRequired()])
    cost = FloatField('Monthly Cost', validators=[DataRequired()])
    renewal_date = DateField(
        'Renewal Date', validators=[DataRequired()], format='%Y-%m-%d'
    )
    submit = SubmitField('Add Subscription')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Update Email')