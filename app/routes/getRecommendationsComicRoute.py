from flask import Blueprint, jsonify
from app.scrape.getRecommendationsComic import getRecommendationsComic

getRecommendationsComicRoute = Blueprint("getRecommendationsComic", __name__)

url = "https://komiku.id/"

@getRecommendationsComicRoute.route("/api/recommended-comic", methods=["GET"])
def get_recommendations_comic(): 
    return jsonify(getRecommendationsComic(url))