from flask import Flask,render_template,request
import pickle
import pandas as pd
app=Flask(__name__)
#load the model 
model=pickle.load(open('saved_model.sav','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    features = ['number_of_bedrooms', 'number_of_bathrooms', 'living_area', 'lot_area',
                'number_of_floors', 'waterfront_present', 'number_of_views',
                'condition_of_the_house', 'grade_of_the_house',
                'area_of_the_house(excluding_basement)', 'area_of_the_basement',
                'built_year', 'renovation_year', 'postal_code', 'lattitude',
                'longitude', 'living_area_renov', 'lot_area_renov',
                'number_of_schools_nearby', 'distance_from_the_airport']
    
    user_input = []
    for feature in features:
        user_input.append(float(request.form[feature]))
    print(user_input)
    # Convert user input to a DataFrame
    df = pd.DataFrame([user_input], columns=features)
    
    # Make prediction
    predicted_price = model.predict(df)[0]
    
    return render_template('result.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)