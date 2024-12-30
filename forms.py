from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, DecimalField, RadioField
from wtforms.validators import DataRequired, NumberRange

class PersonalData(FlaskForm):
    gender= RadioField("Gender", choices=[(0,'Female'),(1,'Male')],default='0',validators=[DataRequired()],description="Choose your gender")
    age = IntegerField("Age", validators=[DataRequired()],description="Specify your age in number")
    income = DecimalField("Income in USD", validators=[DataRequired()],description="Specify your annual salary in USD")
    income_stability = RadioField("Income stability", choices=[(0,'Low'),(1,'High')],default='0',validators=[DataRequired()],description="Choose the stability of your income")
    location = RadioField("Location", choices=[(0,'Rural'),(1,'Semi-Urban'),(3,'Urban')],default='3',validators=[DataRequired()],description="Choose your location")
    loan_amount_req= DecimalField("Required loan amount", validators=[DataRequired()],description="Specify the required loan amount in USD")
    current_loan_amount = DecimalField("Existing monthly loan expenses", validators=[DataRequired()],description="Specify your monthly loan expenses in USD")
    exp_type_1 = RadioField("Have fixed expenses", choices=[(0,'No'),(1,'Yes')],default='0',validators=[DataRequired()],description="Have fixed expenses like rent, mortgage, subscriptions etc.")
    exp_type_2 = RadioField("Have variable expenses", choices=[(0,'No'),(1,'Yes')],default='0',validators=[DataRequired()],description="Have variable expenses like gas, utility etc.")
    dependents = IntegerField("No. of dependents", validators=[NumberRange(min=0)],description="Number of individuals dependent on you financially")
    credit_score = IntegerField("Current credit score",validators=[DataRequired()],description="Specify your current credit score")
    num_defaults = IntegerField("No. of existing credit defaults", validators=[NumberRange(min=0)],description="Specify current number of card defaults")
    active_credit_card = RadioField("Have active credit card", choices=[(0,'Active'),(1,'Inactive'),(2,'Unpossessed')],default='1',validators=[DataRequired()],description="Status of possession of a credit card at present")
    prop_age = DecimalField("Age of the property in years",validators=[DataRequired()],description="Specify the collateral property age in years")
    prop_type = RadioField("Type of property", choices=[(1,'Residential'),(2,'Commercial'),(3,'Industrial'),(4,'Agricultural')],default='1',validators=[DataRequired()],description="Choose the type of your property intended for collateral")
    prop_locn = RadioField("Property Location", choices=[(0,'Semi-Urban'),(1,'Rural'),(3,'Urban')],default='3',validators=[DataRequired()],description="Choose the location of the collateral property")
    co_applicant = RadioField("Have co-applicant",choices=[(0,'No'),(1,'Yes')],default='0',validators=[DataRequired()],description="Do you have a suitable co-applicant")
    prop_price = DecimalField("Price of the property in USD",validators=[DataRequired()],description="Specify the price of the collateral property in USD")
    submit = SubmitField("Submit Post")



