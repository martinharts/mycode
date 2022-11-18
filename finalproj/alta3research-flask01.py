#!/usr/bin/env python3

"""
Flask Library Proficiency Assignment
Tasks:
- at least two endpoints
- at least one of your endpoints should return JSON
- one additional feature (choice: jinja2 logic)
"""

# import Flask: Web application framework
from flask import Flask
# import render_template to show html home page
from flask import render_template
# import josnify to retrun legal JSON text
from flask import jsonify

# create an instance of the Flask object
app = Flask(__name__)

# JSON data for application
masterbikes = [
    {
        "bike": "Ninja 636",
        "price": "$12,000",
        "type": "street bike"
    },
    {
        "bike": "Suzuki GSXR 600",
        "price": "$11,000",
        "type": "street bike"
    },
    {
        "bike": "Honda CRF150R",
        "price": "$5,000",
        "type": "dirt bike"
    },
    {
        "bike": "Yamaha YZ450F",
        "price": "$6,000",
        "type": "dirt bike"
    }
]

# function to return content
# route() tells the application which URL should call the home function
@app.route("/")
def home():
    # Sends back the greeting page
    return render_template("index.html")

# endpoint to return seven wonders of the world
@app.route("/streetbikes")
def street_bikes():
    bikes = []
    for bike in masterbikes:
        if bike["type"] == "street bike":
            bikes.append(bike)

    return render_template("street.html", list = bikes)

# endpoint to return seven natural wonders of the world
@app.route("/dirtbikes")
def dirt_bikes():
    bikes = []
    for bike in masterbikes:
        if bike["type"] == "dirt bike":
            bikes.append(bike)

    return render_template("dirt.html", list = bikes)

# endpoint that returns JSON
@app.route("/all")
def all_wonders():
    # josnify returns legal JSON
    return jsonify(masterbikes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) # runs the application at port 3000