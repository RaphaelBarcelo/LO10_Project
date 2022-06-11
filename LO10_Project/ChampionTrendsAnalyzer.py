# Import TrendReq to connect to Google
import json
import random

from pytrends.request import TrendReq
import Connection
import numpy as np
import time

import Champion
import pandas as pd


def get_champions_trends():
    versions = Connection.watcher.data_dragon.versions_for_region(Connection.region_v4)
    champions_version = versions['n']['champion']
    current_champ_list = Connection.watcher.data_dragon.champions(champions_version)

    pytrends1 = TrendReq()
    all_champions_popularity_comparisons = {}
    for champion in current_champ_list:
        all_champions_popularity_comparisons[champion['name']] = {}
    for champion_1 in current_champ_list:
        champion1_popularity_comparison = {}
        for champion_2 in current_champ_list:
            if champion_1 != champion_2:
                if champion_1 not in all_champions_popularity_comparisons[champion_2]:
                    search_terms = [champion_1['name'] + ' league of legends', champion_2['name'] + ' league of legends']
                    champion1_popularity_comparison[champion_2['name']] = random.randint(0, 100)
                    all_champions_popularity_comparisons[champion_2['name']][champion_1['name']] = random.randint(0, 100)

                    # pytrends1.build_payload(search_terms, geo='US', timeframe="today 12-m")
                    # df1 = pytrends1.interest_over_time()
                    # champion1_popularity_comparison[champion_2['name']] = df1[search_terms[1]].mean().round(0)
                    # all_champions_popularity_comparisons[champion_2['name']][champion_1['name']] = df1[search_terms[0]].mean().round(0)
                    # time.sleep(1.1)

                    # averageList1 = []
                    # for item in searchTerms:
                    #    averageList1.append(df1[item].mean().round(0))
                    # average_by_champion = dict(zip(champions, averageList1))

    all_champions_popularity_rating = {}
    for champion in all_champions_popularity_comparisons:
        comparison = all_champions_popularity_comparisons[champion]
        averageComparisonValues = np.mean(list(comparison.values()))
        all_champions_popularity_rating[champion] = averageComparisonValues

    sorted_champions = sorted(all_champions_popularity_rating.items(), key=lambda x: x[1], reverse=True)

    print(sorted_champions)
    # with open('C://Users//zenit//Desktop//lo10_data_2.txt', 'w') as file:
    #    file.write(json.dumps(all_champions_popularity_rating))
    # with open('C://Users//zenit//Desktop//lo10_data_1.txt', 'w') as file:
    #    file.write(json.dumps(all_champions_popularity_comparisons))

    # print(searchTerms)
    # print(average_by_champion)
