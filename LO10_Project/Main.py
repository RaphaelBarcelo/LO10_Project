from flask import Flask, request, jsonify
from flask_cors import CORS
import ChampionTrendsAnalyzer
from Champion import Champion
from LO10_Project import TeamComposer
from Match import MatchService
import Summoner
import json

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/champions/<champion_name>")
def get_champion_info(champion_name):
    champion = Champion(champion_name)
    return champion.get_summary()


@app.route("/champions/")
def get_all_champion_info():
    return Champion.get_all_champions()


@app.route("/champion_trends/")
def get_champions_trends():
    return jsonify(ChampionTrendsAnalyzer.get_ranking_random())


@app.route("/summoner/<summoner_name>")
def get_summoner_info(summoner_name):
    summoner = Summoner.Summoner(summoner_name)
    return summoner.get_summary()


@app.route("/match/<id>")
def get_match(id):
    match_service = MatchService()
    return match_service.getMatchById(id)


@app.route("/team_composer/", methods=["GET", "POST"])
def assign_lanes():
    data = request.json
    return jsonify(TeamComposer.assign_lanes(data))


if __name__ == "__main__":
    app.run(debug=True)
