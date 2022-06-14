from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

from api.services.Champion import Champion
from api.services.Match import Match
from api.services import Summoner
from api.services import TeamComposer

from api.controllers.MatchController import match_routes
from api.controllers.ChampionController import champion_routes
from api.controllers.SummonerController import summoner_routes
from api.controllers.TeamComposerController import teamComposer_routes
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


app.register_blueprint(champion_routes)
app.register_blueprint(match_routes)
app.register_blueprint(summoner_routes)
app.register_blueprint(teamComposer_routes)


@app.route('/team_composer/', methods=["GET"])
def assign_lanes():
    string_test = request.args['team']
    tab_summ = string_test.split(';')
    return jsonify(TeamComposer.assign_lanes_random(tab_summ))


if __name__ == "__main__":
    app.run(debug=True)
