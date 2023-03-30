from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Model = int(request.form['Model'])
        Model_type = int(request.form['Model_type'])
        Mileage = int(request.form['Model_type'])
        city_mpg = int(request.form['city_mpg'])
        hgwy_mpg = int(request.form['hgwy_mpg'])
        colour = int(request.form['colour'])

        xnew = [Year, Model, Model_type, Mileage, city_mpg, hgwy_mpg, colour]

        a = []
        for i in range(0,27):
            a.append(0)

        a[0] = xnew[0]
        a[1] = xnew[1]
        a[2] = np.log(xnew[3])
        a[3] = np.log(xnew[4])
        a[4] = np.log(xnew[5])
        a[5] = np.log(xnew[0]/xnew[4])
        a[6] = np.log(xnew[3]/xnew[4])
        a[7] = np.log(xnew[3]/xnew[0])

        X_train_columns = ['Year', 'Model', 'mileage', 'city_mpg', 'highway_mpg', 'new_col1',
       'new_col2', 'new_col3', 'Type_bullitt', 'Type_ecoboost', 'Type_gt',
       'Type_gt350', 'Type_gt500', 'Type_mach-e', 'Type_premium',
       'Type_standard', 'car_colour_blue', 'car_colour_gray',
       'car_colour_green', 'car_colour_magnetic', 'car_colour_marron',
       'car_colour_orange', 'car_colour_other', 'car_colour_red',
       'car_colour_silver', 'car_colour_white', 'car_colour_yellow']

        data = [a.copy()]

        d = pd.DataFrame(data,columns=X_train_columns)

        if d['Model'][0] == 'Mustang':
            d['Model'][0] = 0
        else:
            d['Model'][0] = 1

        y_pred = d.iloc[0].tolist()
        prediction = model.predict([y_pred])
        output = round(prediction[0],2)

        return output

if __name__=="__main__":
    app.run(debug=True)

