# Import TrendReq to connect to Google
import csv
import os
import time
import glob
from nordvpn_switcher import initialize_VPN, rotate_VPN
from pytrends.request import TrendReq
import random
import Connection

path = "C://Users//zenit//Desktop//LO10 Project//data/"
champions = {}
problematic_champions = {}


def init_champions():
    print('Initiating champions')
    versions = Connection.watcher.data_dragon.versions_for_region(Connection.region_v4)
    champions_version = versions['n']['champion']
    current_champ_list = Connection.watcher.data_dragon.champions(champions_version)['data']

    for champion in current_champ_list:
        champions[champion] = current_champ_list[champion]['name']
        problematic_champions[champion] = 0
    problematic_champions['DrMundo'] = 4


def create_csv_file():
    for champion, name in champions.items():
        with open(path + champion + ".csv", "w") as my_empty_csv:
            pass


def initiate_csv_file():
    pytrends1 = TrendReq()
    #settings = initialize_VPN(area_input=['complete rotation'])
    while True:
        try:
            for champion_1, champion_1_name in champions.items():
                if os.stat(path + champion_1 + '.csv').st_size == 0 and problematic_champions[champion_1] < 3:
                    champion1_popularity_comparison = {}
                    # rotate_VPN(settings)
                    problematic_champions[champion_1] += 1
                    for champion_2, champion_2_name in champions.items():
                        if champion_1 != champion_2:
                            search_terms = [champion_1_name + ' league of legends',
                                            champion_2_name + ' league of legends']
                            pytrends1.build_payload(search_terms, geo='US', timeframe="today 12-m")
                            df1 = pytrends1.interest_over_time()
                            champion1_popularity_comparison[champion_2] = df1[search_terms[0]].mean().round(0)
                            print(champion_1 + ' : ' + champion_2 + ' (' +
                                  str(champion1_popularity_comparison[champion_2]) + ')')
                            time.sleep(1.1)
                    with open(path + champion_1 + '.csv', 'w') as f:
                        pass
                        #w = csv.writer(f)
                        #w.writerows(champion1_popularity_comparison.items())
            break
        except Exception as e:
            print(e)
            time.sleep(1)
            continue


def get_ranking():
    init_champions()
    champion_ranking = {}
    for file in glob.glob(path):
        trends = []
        with open(file, mode='r') as inp:
            reader = csv.reader(inp)
            for rows in reader:
                trends.append(rows[1])
        average_score = sum(trends) / len(trends)
        champion = os.path.splitext(file)[0]
        champion_ranking[champions[champion]] = average_score
    return champion_ranking


def get_ranking_random():
    init_champions()
    champion_ranking = {}
    for champion, name in champions.items():
        champion_ranking[name] = random.randint(0, 100)
    return champion_ranking


init_champions()
initiate_csv_file()
