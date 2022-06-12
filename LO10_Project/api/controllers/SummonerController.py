from flask import Blueprint
from api.services.Summoner import Summoner
from flask import jsonify

summoner_routes = Blueprint("summoner_routes",__name__,url_prefix="/summoner")

@summoner_routes.route("/<summoner_name>")
def get_summoner_info(summoner_name):
    return Summoner(summoner_name).get_summary()

@summoner_routes.route("/<summoner_name>/matches")
def get_summoner_history(summoner_name):
    return jsonify(Summoner(summoner_name).get_history_matches())
