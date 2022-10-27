from flask import Flask, json, request, jsonify, render_template
from utils import car_price

import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('welcome to flask')
    return render_template("new_home.html")

@app.route('/predict', methods =['POST'])
def get_car_price():
    data=request.form                               #for to get data from user
    print('data is :',data)
    symboling=eval(data['symboling'])
    normalized_losses = eval(data['normalized_losses'])
    fuel_type = data['fuel_type']                  #{'gas':0,'diesel':1}
    aspiration = data['aspiration']                #{'std':0,'turbo':1}
    num_of_doors = data['num_of_doors']            #{'four':4,'two':2}
    engine_location = data['engine_location']      #{'front': 0, 'rear': 1}
    wheel_base = eval(data['wheel_base'])
    length = eval(data['length'])
    width = eval(data['width'])
    height = eval(data['height'])
    curb_weight = eval(data['curb_weight'])
    num_of_cylinders= data['num_of_cylinders'] #{'four': 4,'six': 6,'five': 5,'eight': 8,'two': 2,'three': 3,'twelve': 12}
    engine_size = eval(data['engine_size'])
    bore= eval(data['bore'])
    stroke = eval(data['stroke'])
    compression_ratio= eval(data['compression_ratio'])
    horsepower= eval(data['horsepower'])
    peak_rpm= eval(data['peak_rpm'])
    city_mpg= eval(data['city_mpg'])
    highway_mpg= eval(data['highway_mpg'])
    make = data['make']
    body_style = data['body_style']
    drive_wheels = data['drive_wheels'] 
    engine_type = data['engine_type'] 
    fuel_system = data['fuel_system']
    car_prc = car_price(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg, make, body_style, drive_wheels, engine_type, fuel_system)
    price= car_prc.get_predict_price()

   
    # return render_template('after.html')
    return (f'predicted price of car is: in ${price.round(0)},  In Rs.{(price*80).round(0)}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5005, debug=True)
