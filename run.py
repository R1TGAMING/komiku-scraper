from flask import Flask, jsonify
from app.routes.getTrendingComicRoute import getTrendingComicRoute
from app.routes.getRecommendationsComicRoute import getRecommendationsComicRoute 

app = Flask(__name__)

app.register_blueprint(getTrendingComicRoute)
app.register_blueprint(getRecommendationsComicRoute)

app.errorhandler(Exception)


def handle_global_error(e):
    return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
