from flask import jsonify
import urllib.request
import Connection
import json

class Champion:
    def __init__(self, name):
        name = name.capitalize()
        with urllib.request.urlopen(
                "http://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion/" 
                + name + ".json") as url:
            data = json.loads(url.read().decode())
            champion_data = data['data'][name]
            self.name = champion_data['name']
            self.title = champion_data['title']
            self.lore = champion_data['lore']

    def get_summary(self):
        return jsonify(result={'name': self.name, 'title': self.title, 'lore': self.lore})

    def get_all_champions():
        versions = Connection.watcher.data_dragon.versions_for_region(Connection.region_v4)
        champions_version = versions['n']['champion']
        current_champ_list_file = Connection.watcher.data_dragon.champions(champions_version)
        current_champ_list = []
        for champion in current_champ_list_file['data']:
            champion_data = current_champ_list_file['data'][champion]
            current_champ_list.append({
                                        'name': champion_data['name'], 
                                        'full': champion_data['image']['full'],
                                        'sprite': champion_data['image']['sprite']
                                      })
        return jsonify(result=current_champ_list)

    