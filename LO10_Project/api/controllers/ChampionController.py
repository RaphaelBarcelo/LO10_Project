from flask import Blueprint
from api.services.Champion import Champion
from api.services.ChampionTrendsAnalyzer import get_champions_trends
champion_routes = Blueprint("champions_routes",__name__,url_prefix="/champions")

@champion_routes.route('/')
def get_all_champion_info():
    return Champion.get_all_champions()

@champion_routes.route("/<champion_name>")
def get_champion_info(champion_name):
    return Champion(champion_name).get_summary()

@champion_routes.route("/trends")
def __get_champions_trends():
    return get_champions_trends()



