from flask import jsonify
from numpy import mat
from riotwatcher import ApiError
import Connection as Connection

class MatchService:
    def __init__(self):
        self.MatchAPI = Connection.watcher.match
    
    def getMatchById(self, id):
        try:
            result = self.MatchAPI.by_id(Connection.region_v4, id)
            return jsonify(result)
        except ApiError as err:
            print(err)
