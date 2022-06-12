from flask import Blueprint
from api.services.Match import Match
from flask import jsonify

match_routes = Blueprint("match_routes",__name__,url_prefix="/match")

@match_routes.route("/<id>")
def get_match_by_id(id):
    matchData = Match().getMatchById(id)
    return jsonify(matchData)
