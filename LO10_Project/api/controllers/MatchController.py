from flask import Blueprint
from LO10_Project.api.services.Match import Match
from flask import jsonify

match_routes = Blueprint("match_routes",__name__,url_prefix="/match")


@match_routes.route("/<id>")
def get_match_by_id(testid):
    matchData = Match().getMatchById(testid)
    return jsonify(matchData)
