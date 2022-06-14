from flask import jsonify
from numpy import mat
from riotwatcher import ApiError
import Connection as Connection

class Match:
    def __init__(self):
        self.MatchAPI = Connection.watcher.match
    
    def getMatchById(self, match_id):
        try:
            result = self.MatchAPI.by_id(Connection.region_v4, match_id)
            return result
        except ApiError as err:
            print(err)

