from flask import Flask

from LO10_Project import ChampionTrendsAnalyzer
from LO10_Project.Champion import Champion
from LO10_Project.Summoner import Summoner

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/champion/<champion_name>")
def get_champion_info(champion_name):
    champion = Champion.Champion(champion_name)
    return champion.get_summary()


@app.route("/champion_trends/")
def get_champions_trends():
    return ChampionTrendsAnalyzer.get_champions_trends()


@app.route("/summoner/<summoner_name>")
def get_champions_trends(summoner_name):
    summoner = Summoner.Summoner(summoner_name)
    return summoner.get_summary()


@app.route("/team_composer/<summoner_name>")
def assign_lanes(summoner_name):
    summoner = Summoner.Summoner(summoner_name)
    return summoner.get_summary()
