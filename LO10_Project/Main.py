from flask import Flask, request, jsonify
from flask_cors import CORS

from api.services.Champion import Champion
from api.services.Match import Match
from api.services import Summoner
from api.services import ChampionTrendsAnalyzer
from api.controllers.ChampionController import champion_routes
from api.controllers.MatchController import match_routes
from api.controllers.SummonerController import summoner_routes
from api.services import TeamComposer

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


app.register_blueprint(champion_routes)
app.register_blueprint(match_routes)
app.register_blueprint(summoner_routes)


# @app.route("/champions/<champion_name>")
# def get_champion_info(champion_name):
#     champion = Champion(champion_name)
#     return Champion.get_summary()


# @app.route("/champions/")
# def get_all_champion_info():
#     return Champion.get_all_champions()

# @app.route("/champion_trends/")
# def get_champions_trends():
#     return ChampionTrendsAnalyzer.get_champions_trends()


# @app.route("/summoner/<summoner_name>")
# def get_summoner_info(summoner_name):
#     summoner = Summoner.Summoner(summoner_name)
#     return summoner.get_summary()

# @app.route("/match/<id>")
# def get_match(id):
#     match_service = Match()
#     return match_service.getMatchById(id)

# @app.route("/team_composer/<summoner_name>")
# def assign_lanes(summoner_name):
#     summoner = Summoner.Summoner(summoner_name)
#     return summoner.get_summary()

# @app.route('/team_composer/', methods=["GET", "POST"])
# def assign_lanes():
#     if request.method == 'POST':
#         data = request.json
#         return jsonify(TeamComposer.assign_lanes(data))


if __name__ == "__main__":
    app.run(debug=True)
