from flask import Blueprint, jsonify
from app.scrape.getTrendingComic import getTrendingComic

getTrendingComicRoute = Blueprint("getTrendingComicRoute", __name__)

url = "https://komiku.id/"


@getTrendingComicRoute.route("/api/trending-comic", methods=["GET"])
def get_trending_comic():
    return jsonify(getTrendingComic(url))
