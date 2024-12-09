
from distutils.command.config import config
from flask import Flask ,jsonify, render_template,request
from models.utils import AutoData

import config

app = Flask(__name__)

@app.route("/")
def hello():
    print("hello flask")
    return render_template("index.html")

@app.route("/predicted_price",methods = ["POST","GET"])
def get_predicted_price():
    print("===================")

    if request.method == "GET":
        print("we are using gate method ")
    # data = request.form

    # symboling = eval(data["symboling"])
    # normalized_losses =eval(data["normalized_losses"])
    # fuel_type = data["fuel_type"]
    # aspiration= data["aspiration"]
    # num_of_doors= data["num_of_doors"]
    # drive_wheels=data["drive_wheels"]
    # engine_location= data["engine_location"]
    # wheel_base=eval(data["wheel_base"])
    # length=eval(data["length"])
    # width=eval(data["width"])
    # height=eval(data["height"])
    # curb_weight=eval(data["curb_weight"])
    # num_of_cylinders= data["num_of_cylinders"]
    # engine_size=eval(data["engine_size"])
    # bore=eval(data["bore"])
    # stroke=eval(data["stroke"])
    # compression_ratio=eval(data["compression_ratio"])
    # horsepower=eval(data["horsepower"])
    # peak_rpm=eval(data["peak_rpm"])
    # city_mpg=eval(data["city_mpg"])
    # highway_mpg=eval(data["highway_mpg"])

    # # one hot encoded 
    # make = data["make"]
    # body_style =data["body_style"]
    # engine_type = data["engine_type"]
    # fuel_system = data["fuel_system"]

        symboling = int(request.args.get("symboling"))
        normalized_losses =int(request.args.get("normalized_losses"))
        fuel_type = request.args.get("fuel_type")
        aspiration= request.args.get("aspiration")
        num_of_doors= request.args.get("num_of_doors")
        drive_wheels=request.args.get("drive_wheels")
        engine_location= request.args.get("engine_location")
        wheel_base=int(request.args.get("wheel_base"))
        length=int(request.args.get("length"))
        width=int(request.args.get("width"))
        height=int(request.args.get("height"))
        curb_weight=int(request.args.get("curb_weight"))
        num_of_cylinders= request.args.get("num_of_cylinders")
        engine_size=int(request.args.get("engine_size"))
        bore=float(request.args.get("bore"))
        stroke=float(request.args.get("stroke"))
        compression_ratio=float(request.args.get("compression_ratio"))
        horsepower=int(request.args.get("horsepower"))
        peak_rpm=int(request.args.get("peak_rpm"))
        city_mpg=int(request.args.get("city_mpg"))
        highway_mpg=int(request.args.get("highway_mpg"))

        # one hot encoded 
        make =request.args.get("make")
        body_style =request.args.get("body_style")
        engine_type = request.args.get("engine_type")
        fuel_system = request.args.get("fuel_system")

        auti_ins = AutoData(symboling, normalized_losses, fuel_type, aspiration,
        num_of_doors, drive_wheels, engine_location, wheel_base,
        length, width, height, curb_weight, num_of_cylinders,
        engine_size, bore, stroke, compression_ratio, horsepower,
        peak_rpm, city_mpg, highway_mpg,make,body_style,
        engine_type,fuel_system)

        price = auti_ins.predicted_price()
        print("Success")

        return render_template("index.html",prediction = price)

    

       
if __name__ == "__main__":
    app.run()
