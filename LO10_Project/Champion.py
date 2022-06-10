import urllib.request, json

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