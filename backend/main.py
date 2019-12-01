from flask import Flask, request, abort, json, jsonify
import googlemaps
from pymongo import MongoClient
from flask_cors import CORS

db = MongoClient('')
key = ''
gmaps = googlemaps.Client(key=key)

app = Flask(__name__)
CORS(app)


@app.route("/get_ingredients", methods=["POST"])
def ingredients():
    resp = request.json
    json_ = {
        "description": "",
        "photo": "",
        "ingredients": {},
        "list": {},
        "name": resp['name']
    }
    cursor = db.data.recipes.find({"name": resp['name']})
    for i in cursor:
        json_["description"] = i['description']
        json_["photo"] = i["photo"]
        for l, m in i['ingredients'].items():
            json_["ingredients"][l] = ' '.join([l,m])

#    for i in cursor:
#        for l, m in i['prices'].items():
#            json_["list"][l] = m

    return jsonify(json_)
@app.route("/get_dishes", methods=["POST"])
def dishes():
    resp = request.json
    print(resp)
    json_ = {
        "dishes": [],
        "urls": []
    }
    cursor = db.data.recipes.find({"region": resp['region']})
    for j, i in enumerate(cursor):
        json_["dishes"].append(i["name"])
        json_["urls"].append(i["photo"])
        if j == 9:
            return jsonify(json_)
    return jsonify(json_)


@app.route("/get_shops", methods=["GET"])
def shops():
    json_ = {
        "shops": [
        ]
    }
    coordinates = request.args.get('cordinates')
    print(coordinates, [coordinates])
    result = gmaps.places_nearby(name='перекресток', radius=3000, location=coordinates,
                                 language="RU")
    for j, i in enumerate(result["results"]):
        json_["shops"].append((i["geometry"]["location"]['lat'], i["geometry"]["location"]['lng']))

    result = gmaps.places_nearby(name='пятёрочка', radius=3000, location=coordinates,
                                 language="RU")
    for j, i in enumerate(result["results"]):
        json_["shops"].append((i["geometry"]["location"]['lat'], i["geometry"]["location"]['lng']))

    return jsonify(json_)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8091)
