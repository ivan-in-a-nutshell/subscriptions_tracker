from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired, Email

class SubscriptionForm(FlaskForm):
    name = StringField('Service Name', validators=[DataRequired()], render_kw={"placeholder": "Netflix, etc."})
    cost = FloatField('Monthly Cost', validators=[DataRequired()], render_kw={"placeholder": "Enter price"})
    renewal_date = DateField(
        'Renewal Date', validators=[DataRequired()], format='%Y-%m-%d'
    )
    submit = SubmitField('Add Subscription')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "email@example.com"})
    submit = SubmitField('Update Email')