from flask import Flask
from flask_cors import CORS
import ChampionTrendsAnalyzer
import Champion
import Summoner

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/champions/<champion_name>")
def get_champion_info(champion_name):
    champion = Champion.Champion(champion_name)
    return Champion.get_summary()


@app.route("/champions/")
def get_all_champion_info():
    return Champion.get_all_champions()


@app.route("/champion_trends/")
def get_champions_trends():
    return ChampionTrendsAnalyzer.get_champions_trends()


@app.route("/summoner/<summoner_name>")
def get_summoner_info(summoner_name):
    summoner = Summoner.Summoner(summoner_name)
    return summoner.get_summary()


@app.route("/team_composer/<summoner_name>")
def assign_lanes(summoner_name):
    summoner = Summoner.Summoner(summoner_name)
    return summoner.get_summary()

if __name__ == "__main__":
    app.run(debug=True)