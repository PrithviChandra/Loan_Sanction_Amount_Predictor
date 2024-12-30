from flask import Flask, render_template
from forms import PersonalData
import numpy as np
from flask_bootstrap import Bootstrap5
import joblib
import warnings
warnings.filterwarnings("ignore")
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
Bootstrap5(app)

model = joblib.load('saved_model/random_forest_model.pkl')
scaler = joblib.load('saved_model/scaler.pkl')

@app.route('/',methods=['GET','POST'])
def index():
    form = PersonalData()
    prediction = None
    if form.validate_on_submit():
    
        gender= int(form.gender.data)
        age = int(form.age.data)
        income = float(form.income.data)
        income_stability = int(form.income_stability.data)
        location = int(form.location.data)
        loan_amount_req= float(form.loan_amount_req.data)
        current_loan_amount = float(form.current_loan_amount.data)
        exp_type_1 = int(form.exp_type_1.data)
        exp_type_2 = int(form.exp_type_2.data)
        dependents = int(form.dependents.data)
        credit_score = float(form.credit_score.data)
        num_defaults = int(form.num_defaults.data)
        active_credit_card = int(form.active_credit_card.data)
        prop_age = float(form.prop_age.data)
        prop_type = int(form.prop_type.data)
        prop_locn = int(form.prop_locn.data)
        co_applicant = int(form.co_applicant.data)
        prop_price = float(form.prop_price.data)

        input = np.array([[gender,age,income,income_stability,location,loan_amount_req,current_loan_amount,exp_type_1,exp_type_2,dependents,credit_score,num_defaults,active_credit_card,prop_age,prop_type,prop_locn,co_applicant,prop_price]],dtype=object)
        pred = model.predict(input)
        print(input)
        for item in input[0]:
            print(type(item))
        prediction = round(scaler.inverse_transform(pred.reshape(-1, 1))[0][0],2)

    return render_template("index.html", form=form, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5002)