from flask import Blueprint, jsonify
from app.scrape.getChapter import getChapter

getChapterComicRoute = Blueprint("getChapterRoute", __name__)

@getChapterComicRoute.route("/api/comic/<title>/<chapter>", methods=["GET"])
def getChapterRoute(title, chapter):
    title = '-'.join(title.split())
    url = f"https://komiku.id/{title.lower()}-chapter-{chapter}/"
    return jsonify(getChapter(url, title))

