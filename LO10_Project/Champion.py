import json
import urllib.request


class Champion:

    def __init__(self, name):
        name = name.capitalize()
        with urllib.request.urlopen(
                "http://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion/" + name + ".json") as url:
            data = json.loads(url.read().decode())
            champion_data = data['data'][name]
            self.name = champion_data['name']
            self.title = champion_data['title']
            self.lore = champion_data['lore']

    def get_summary(self):
        return {'name': self.name, 'title': self.title, 'lore': self.lore}
