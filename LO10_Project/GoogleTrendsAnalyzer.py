#Import TrendReq to connect to Google
from pytrends.request import TrendReq

def sort_by_popularity(champions):
    searchTerms = []
    for champion in champions:
        searchTerms.append(champion + ' League Of Legends')
    pytrends1 = TrendReq()
    pytrends1.build_payload(searchTerms, geo='US', timeframe="today 12-m")
    df1 = pytrends1.interest_over_time()
    averageList1 = []
    for item in searchTerms:
        averageList1.append(df1[item].mean().round(0))
    average_by_champion = dict(zip(champions, averageList1))
    print(searchTerms)
    print(average_by_champion)