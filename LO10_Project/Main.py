from flask import Flask, request, jsonify
from flask_cors import CORS
<<<<<<< HEAD
=======
import ChampionTrendsAnalyzer
from Champion import Champion
from LO10_Project import TeamComposer
from Match import MatchService
import Summoner
import json
>>>>>>> cb014d3daac6b718cd0552adc5a984ce6a13ad5d

from api.services.Champion import Champion
from api.services.Match import Match
from api.services import Summoner
from api.services import ChampionTrendsAnalyzer

from api.controllers.MatchController import match_routes
from api.controllers.ChampionController import champion_routes
from api.controllers.SummonerController import summoner_routes
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"

app.register_blueprint(champion_routes)
app.register_blueprint(match_routes)
app.register_blueprint(summoner_routes)

<<<<<<< HEAD
# @app.route("/champions/<champion_name>")
# def get_champion_info(champion_name):
#     champion = Champion(champion_name)
#     return Champion.get_summary()
=======
@app.route("/champions/<champion_name>")
def get_champion_info(champion_name):
    champion = Champion(champion_name)
    return champion.get_summary()
>>>>>>> cb014d3daac6b718cd0552adc5a984ce6a13ad5d


# @app.route("/champions/")
# def get_all_champion_info():
#     return Champion.get_all_champions()

<<<<<<< HEAD
# @app.route("/champion_trends/")
# def get_champions_trends():
#     return ChampionTrendsAnalyzer.get_champions_trends()
=======

@app.route("/champion_trends/")
def get_champions_trends():
    return jsonify(ChampionTrendsAnalyzer.get_ranking_random())
>>>>>>> cb014d3daac6b718cd0552adc5a984ce6a13ad5d


# @app.route("/summoner/<summoner_name>")
# def get_summoner_info(summoner_name):
#     summoner = Summoner.Summoner(summoner_name)
#     return summoner.get_summary()

<<<<<<< HEAD
# @app.route("/match/<id>")
# def get_match(id):
#     match_service = Match()
#     return match_service.getMatchById(id)

# @app.route("/team_composer/<summoner_name>")
# def assign_lanes(summoner_name):
#     summoner = Summoner.Summoner(summoner_name)
#     return summoner.get_summary()
=======

@app.route("/match/<id>")
def get_match(id):
    match_service = MatchService()
    return match_service.getMatchById(id)


@app.route("/team_composer/", methods=["GET", "POST"])
def assign_lanes():
    data = request.json
    return jsonify(TeamComposer.assign_lanes(data))

>>>>>>> cb014d3daac6b718cd0552adc5a984ce6a13ad5d

if __name__ == "__main__":
    app.run(debug=True)
