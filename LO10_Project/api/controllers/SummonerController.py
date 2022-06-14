from urllib import response
from flask import Blueprint
from LO10_Project.api.services.Summoner import Summoner
from flask import jsonify
from riotwatcher import ApiError

summoner_routes = Blueprint("summoner_routes",__name__,url_prefix="/summoner")


@summoner_routes.route("/<summoner_name>")
def get_summoner_info(summoner_name):
    try:
        response = Summoner(summoner_name).get_summary()
        return jsonify(response)
    except ApiError as err:
        return jsonify(error=err.response.status_code, message="Not Found"), err.response.status_code


@summoner_routes.route("/<summoner_name>/matches")
def get_summoner_history(summoner_name):
    return jsonify(Summoner(summoner_name).get_history_matches())

