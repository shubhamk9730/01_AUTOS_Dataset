import numpy as np
import pickle
import json

class car_price():
    def __init__(self,symboling, normalized_losses,fuel_type,aspiration,num_of_doors,engine_location,wheel_base,
    length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,
    peak_rpm,city_mpg,highway_mpg, make, body_style, drive_wheels, engine_type, fuel_system):
        
        self.symboling =symboling
        self.normalized_losses =normalized_losses
        self.fuel_type =fuel_type                  #{'gas':0,'diesel':1}
        self.aspiration =aspiration                #{'std':0,'turbo':1}
        self.num_of_doors =num_of_doors            #{'four':4,'two':2}
        self.engine_location =engine_location      #{'front': 0, 'rear': 1}
        self.wheel_base =wheel_base
        self.length =length
        self.width =width
        self.height =height
        self.curb_weight =curb_weight
        self.num_of_cylinders=num_of_cylinders #{'four': 4,'six': 6,'five': 5,'eight': 8,'two': 2,'three': 3,'twelve': 12}
        self.engine_size =engine_size
        self.bore=bore
        self.stroke =stroke 
        self.compression_ratio=compression_ratio
        self.horsepower=horsepower
        self.peak_rpm=peak_rpm
        self.city_mpg=city_mpg
        self.highway_mpg=highway_mpg
        self.make = 'make_'+make
        self.body_style = 'body-style_' +body_style
        self.drive_wheels = 'drive-wheels_' +drive_wheels
        self.engine_type = 'engine-type_' +engine_type
        self.fuel_system = 'fuel-system_' +fuel_system

    def load_model(self):
        with open('linear_model.pkl', 'rb') as f:
            self.model= pickle.load(f)

        with open('project_data.json', 'r') as f:
            self.json_data = json.load(f)

    def get_predict_price(self):
        self.load_model()
        make_index = self.json_data['columns'].index(self.make)
        body_style_index = self.json_data['columns'].index(self.body_style)
        drive_wheels_index = self.json_data['columns'].index(self.drive_wheels)
        engine_type_index = self.json_data['columns'].index(self.engine_type)
        fuel_system_index = self.json_data['columns'].index(self.fuel_system)

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.symboling                                   
        test_array[1] = self.normalized_losses                           
        test_array[2] = self.json_data['fuel_type'][self.fuel_type]       
        test_array[3] = self.json_data['aspiration'][self.aspiration]      
        test_array[4] = self.json_data['num_of_doors'][self.num_of_doors]  
        test_array[5] = self.json_data['engine_location'][self.engine_location]
        test_array[6] = self.wheel_base                                  
        test_array[7] = self.length                                      
        test_array[8] = self.width                                       
        test_array[9] = self.height                                      
        test_array[10]= self.curb_weight                                 
        test_array[11]= self.json_data['num_of_cylinders'][self.num_of_cylinders]
        test_array[12]= self.engine_size                                 
        test_array[13]= self.bore                                        
        test_array[14]= self.stroke                                      
        test_array[15]= self.compression_ratio                          
        test_array[16]= self.horsepower                                 
        test_array[17]= self.peak_rpm                                   
        test_array[18]= self.city_mpg                                   
        test_array[19]= self.highway_mpg                                
        test_array[make_index]= 1                                  
        test_array[body_style_index] =1            
        test_array[drive_wheels_index] =1      
        test_array[engine_type_index] =1           
        test_array[fuel_system_index] =1

        print('Test Array :', test_array)
        predict_charges = (self.model.predict([test_array])[0])
        print(predict_charges)
        return predict_charges
    
if __name__ == '__main__':
    symboling = 3
    normalized_losses = 90
    fuel_type = 'gas'             
    aspiration = 'turbo'          
    num_of_doors = 'four'         
    engine_location = 'front'      
    wheel_base = 100
    length = 250
    width = 150
    height = 100
    curb_weight = 2000
    num_of_cylinders= 'twelve'    
    engine_size = 150
    bore= 5.5
    stroke = 4.8 
    compression_ratio= 10
    horsepower= 250 
    peak_rpm= 8000
    city_mpg= 25
    highway_mpg= 29
    make = 'audi'
    body_style = 'sedan'
    drive_wheels = '4wd'
    engine_type = 'dohc'
    fuel_system = 'mfi'
    car_prc = car_price(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg, make, body_style, drive_wheels, engine_type, fuel_system)
    car_prc.get_predict_price()