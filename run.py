from flask import Flask, jsonify
from app.routes.getTrendingComicRoute import getTrendingComicRoute

app = Flask(__name__)

app.register_blueprint(getTrendingComicRoute)

app.errorhandler(Exception)


def handle_global_error(e):
    return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
