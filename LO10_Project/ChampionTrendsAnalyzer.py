# Import TrendReq to connect to Google
import json
import random
from pytrends.request import TrendReq
import Connection
import numpy as np
import time
import pandas as pd


def get_champions_trends():
    pytrends1 = TrendReq()
    versions = Connection.watcher.data_dragon.versions_for_region(Connection.region_v4)
    champions_version = versions['n']['champion']
    current_champ_list = Connection.watcher.data_dragon.champions(champions_version)

    all_champions_trends_comparisons = {}
    for champion_1 in current_champ_list:
        for champion_2 in current_champ_list:
            all_champions_trends_comparisons[champion_1] = {champion_2: ''}
    df = pd.DataFrame.from_dict(all_champions_trends_comparisons, orient='index')  # convert dict to dataframe
    df.to_csv('C://Users//zenit//Desktop//lo10_project_data.csv')

    for champion_1 in all_champions_trends_comparisons:
        df = pd.read_csv("C://Users//zenit//Desktop//lo10_project_data.csv")  # or pd.read_excel(filename) for xls file
        all_champions_trends_comparisons = df.to_dict(orient='index')
        for champion_2 in all_champions_trends_comparisons:
            if champion_1 != champion_2:
                if champion_1[champion_2] == '' \
                        or champion_1[champion_2] == ' '\
                        or champion_1[champion_2] is None:
                    search_terms = [champion_1 + ' league of legends', champion_2 + ' league of legends']
                    #all_champions_trends_comparisons[champion_1][champion_2] = random.randint(0, 100)
                    #all_champions_trends_comparisons[champion_2][champion_1] = random.randint(0, 100)
                    pytrends1.build_payload(search_terms, geo='US', timeframe="today 12-m")
                    df1 = pytrends1.interest_over_time()
                    champion_1[champion_2] = df1[search_terms[1]].mean().round(0)
                    champion_2[champion_1] = df1[search_terms[0]].mean().round(0)
                    time.sleep(1.1)
        df = pd.DataFrame.from_dict(all_champions_trends_comparisons, orient='index')  # convert dict to dataframe
        df.to_csv('C://Users//zenit//Desktop//lo10_project_data.csv')

    all_champions_popularity_rating = {}
    for champion in all_champions_trends_comparisons:
        comparison = all_champions_trends_comparisons[champion]
        average_comparison_values = np.mean(list(comparison.values()))
        all_champions_popularity_rating[champion] = average_comparison_values

    sorted_champions = sorted(all_champions_popularity_rating.items(), key=lambda x: x[1], reverse=True)

    print(sorted_champions)
    with open('C://Users//zenit//Desktop//lo10_data.txt', 'w') as file:
        file.write(json.dumps(sorted_champions))