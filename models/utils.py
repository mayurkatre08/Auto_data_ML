from distutils.command.config import config
import pandas as pd
import numpy as np
import pickle
import json
try:
    import config
except:
    pass


class AutoData():
    def __init__(self,symboling ,normalized_losses ,fuel_type ,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,
        length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,
        city_mpg,highway_mpg,make ,body_style,engine_type ,fuel_system ) :

        self.symboling =symboling
        self.normalized_losses =normalized_losses
        self.fuel_type =fuel_type
        self.aspiration=aspiration
        self.num_of_doors=num_of_doors
        self.drive_wheels=drive_wheels
        self.engine_location=engine_location
        self.wheel_base=wheel_base
        self.length=length
        self.width=width
        self.height=height
        self.curb_weight=curb_weight
        self.num_of_cylinders=num_of_cylinders
        self.engine_size=engine_size
        self.bore=bore
        self.stroke=stroke
        self.compression_ratio=compression_ratio
        self.horsepower=horsepower
        self.peak_rpm=peak_rpm
        self.city_mpg=city_mpg
        self.highway_mpg=highway_mpg
        self.make = "make_" + make
        self.body_style = "body-style_" + body_style 
        self.engine_type = "engine-type_" + engine_type
        self.fuel_system = "fuel-system_" + fuel_system

    def load_model(self):
        try:
            with open(config.MODEL_FILE_PATH,"rb") as f:
                self.model = pickle.load(f)
        except:
            with open("Adaboost.pkl","rb") as f:
                self.model = pickle.load(f)

        try:
            with open(config.JSON_FILE_PATH,"r")as f:
                self.json_data = json.load(f)

        except:
            with open("label_encoded_dict.json","r")as f:
                self.json_data = json.load(f)

    def predicted_price(self):
        self.load_model()

        make_index  = self.json_data["column_name"].index(self.make)
        body_style_index = self.json_data["column_name"].index(self.body_style)
        engine_type_index = self.json_data["column_name"].index(self.engine_type)
        fuel_system_index = self.json_data["column_name"].index(self.fuel_system)

        array = np.zeros(len(self.json_data["column_name"]))

        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_data["fuel_type_dict"][self.fuel_type]
        array[3] = self.json_data["aspiration_dict"][self.aspiration]
        array[4] = self.json_data["num_of_doors_dict"][self.num_of_doors]
        array[5] = self.json_data["drive_wheel_dict"][self.drive_wheels]
        array[6] = self.json_data["engine_location_dict"][self.engine_location]
        array[7] = self.wheel_base
        array[8] = self.length
        array[9] = self.width
        array[10] = self.height
        array[11] = self.curb_weight
        array[12] = self.json_data["num_of_cylinder_dict"][self.num_of_cylinders]
        array[13] = self.engine_size
        array[14] = self.bore
        array[15] = self.stroke
        array[16] = self.compression_ratio
        array[17] = self.horsepower
        array[18] = self.peak_rpm
        array[19] = self.city_mpg
        array[20] = self.highway_mpg


        array[body_style_index] = 1
        array[engine_type_index] = 1
        array[fuel_system_index] = 1
        array[make_index] = 1

        predicted_price = self.model.predict([array])[0]
        # print("predicted_price",predicted_price)
        return np.around(predicted_price,2)

if __name__ == "__main__":
    symboling = 3.0
    normalized_losses = 115.0
    fuel_type = 'diesel'
    aspiration= 'turbo'
    num_of_doors= 'two'
    drive_wheels= 'rwd'
    engine_location= 'front'
    wheel_base=88.60
    length=168.80
    width=64.10
    height=48.80
    curb_weight=2548.00
    num_of_cylinders= 'six'
    engine_size=130.00
    bore=3.47
    stroke=2.68
    compression_ratio=9.00
    horsepower=111.00
    peak_rpm=5000.00
    city_mpg=21.00
    highway_mpg=27.00


    make = "alfa-romero"
    body_style = "convertible"
    engine_type = "dohc"
    fuel_system = "1bbl"

    obj = AutoData(symboling ,normalized_losses ,fuel_type ,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,
        length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,
        city_mpg,highway_mpg,make ,body_style,engine_type ,fuel_system )
    price = obj.predicted_price()
    print(f"predicted price of car the is {price} /- Rs Only")