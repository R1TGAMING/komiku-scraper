from flask import Blueprint, jsonify, request
from app.scrape.getComicByName import getComicByName

getComicByNameRoute = Blueprint("getComicByNameRoute", __name__)

@getComicByNameRoute.route("/api/comic", methods=["GET"])
def get_recommendations_comic(): 
    name = request.args.get('name')
    url = f"https://api.komiku.id/?post_type=manga&s={name}"
    return jsonify(getComicByName(url))
