from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

Profile = {
     "success": True,
     "data": {
        "last_updated": "2/3/2021, 8:48:51 PM",
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
     }
}

Tank = []
num = 0

@app.route("/")
def home():
    return "ECSE 3038 LAB 2"

@app.route("/profile", methods=["GET", "POST", "PATCH"])
def getting_profile():
    if request.method == "GET":
        return jsonify(Profile)

    elif request.method == "POST":
        # Get the current date and time
        now = datetime.now()
        datetimee = now.strftime("%d/%m/%Y %H:%M:%S")

        Profile["data"]["last_updated"] = (datetimee)
        Profile["data"]["username"] = (request.json["username"])
        Profile["data"]["role"] = (request.json["role"])
        Profile["data"]["color"] = (request.json["color"])

        return jsonify(Profile)

    elif request.method == "PATCH":
        # Get the current date and time
        now = datetime.now()
        datetimee = now.strftime("%d/%m/%Y %H:%M:%S")
    
        data = Profile["data"]

        r = request.json
        r["last_updated"] = datetimee
        attributes = r.keys()
        for attribute in attributes:
            data[attribute] = r[attribute]

        return jsonify(Profile)    

@app.route("/data", methods=["GET", "POST"])
def tank_data():
    if request.method == "GET":
        return jsonify(Tank)  

    elif request.method == "POST":
        global num

        num = num + 1

        r = request.json
        r["id"] = num
        Tank.append(r)
        return jsonify(Tank)

@app.route('/data/<int:id>', methods=["PATCH", "DELETE"])
def tank_id_methods(id):
    if request.method == "PATCH":
        for i in Tank:
            if i["id"] == id:
                r = request.json
                attributes = r.keys()

                for attribute in attributes:
                    i[attribute] = r[attribute]

        return jsonify(Tank)
    
    elif request.method == "DELETE":
        for i in Tank:
            if i["id"] == id:
                Tank.remove(i)

        return jsonify(Tank)


if __name__ == '__main__' :
    app.run()
    debug=True
    port = 5000