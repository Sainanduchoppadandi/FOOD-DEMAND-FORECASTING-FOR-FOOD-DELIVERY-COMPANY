# import the necessary packages
import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask,request, render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def about():
    return render_template('home.html')
 #@app.route('/pred')
#def page():
   # return render_template('upload.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        print("[INFO] loading model...")
        model = pickle.load(open('model.pkl', 'rb'))
        input_features = [float(x) for x in request.form.values()]
        features_value = [np.array(input_features)]
        print(features_value)
        
        features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine',
        'city_code', 'region_code', 'category']
        prediction = model.predict(features_value)
        output=prediction[0]    
        print(output)
        return render_template('upload.html', output=output)
    return render_template('upload.html')

if __name__ == '__main__':
      app.run(debug=True)
 