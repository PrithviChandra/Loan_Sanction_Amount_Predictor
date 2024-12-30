# Loan_Sanction_Amount_Predictor
An application to predict loan amount based on customer's personal data, built using a random forest regression model

Demo: https://loan-sanction-amount-predictor.onrender.com

- Data was collected from Kaggle, Contains ~30000 records. The data is not completely authentic.
- Data was preprocessed by removing NaN, outlier detection and removal using z-score technique, typecasting, reducing skewness and scaled using standard scaler. 5 models (Gradient Boost, Random Forest, Linear Regression, PCA based linear regression, Neural Network) was tried to fit the model to predict eligible loan amount based on the user's personal data. 
- Random Forest model performed the best with a MSE of 0.04 on the test data.
- The data was separately trained using random forest model after additional data transformations like converting the property age feature into 'No. of Years' format.
- The resultant model and scaler were saved using Pickle.
- A Flask based application was created to give realtime estimates to users about approx loan amount eligibility.
- Technologies used: Pandas, Matplotlib, Seaborn, Scikit-Learn, joblib, Flask, Jinja2, Flask-WTForms, Cross-Site Request Forgery as part of WTForms, HTML, CSS, PyTorch, Bootstrap5, HTML, CSS

Future Scope:
- Data can be improved to enhance representation especially for feature like gender etc
- Data quality can be enhanced
- The Flask app ca integrate a database to store user provided data for R&D 
- Trained and tested using gradient boost regressor, random forest regressor, neural network, linear regressor with and without Principal Component Analysis. The best performance was rendered by random forest regressor
