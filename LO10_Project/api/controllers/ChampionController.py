import this
from flask import Blueprint
from flask import jsonify

from LO10_Project.api.services.Champion import Champion

champion_routes = Blueprint("champions_routes",__name__,url_prefix="/champions")

@champion_routes.route('/')
def get_all_champion_info():
    data = Champion.get_all_champions(this)
    return jsonify(result=data)

@champion_routes.route("/<champion_name>")
def get_champion_info(champion_name):
    data = Champion(champion_name).get_summary()
    return jsonify(data)

# @champion_routes.route("/trends")
# def __get_champions_trends():
#     return get_champions_trends()



