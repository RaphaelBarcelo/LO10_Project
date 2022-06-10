from flask import Flask

from LO10_Project import ChampionTrendsAnalyzer
from LO10_Project.Champion import Champion
from LO10_Project.Summoner import Summoner

ChampionTrendsAnalyzer.get_champions_trends()
