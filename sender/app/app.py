from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime as dt

import geocoder

app = Flask(__name__)
api = Api(app)

class TimeHandler(Resource):
    def get(self):
        currenttime_now = dt.now()

        return {"message": f"{currenttime_now.time()}"}

class LocationHandler(Resource):
    def get(self):
        g = geocoder.ip('me')
        # print(g.latlng)

        return {"message": f"{g}"}


api.add_resource(TimeHandler, "/get-time")
api.add_resource(LocationHandler, "/get-location")


if __name__ == "__main__":
    app.run(debug=True, port=5051, host="0.0.0.0")
