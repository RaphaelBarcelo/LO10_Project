import Connection as Connection
import Summoner
import GoogleTrendsAnalyzer as GoogleTrendAnalyzer

summoner_doublelift = Summoner.Summoner('Doublelift')

summoner_fake_doublelift = Summoner.Summoner('Doublelift')

summoner_top = Summoner.Summoner('a')
summoner_jungle = Summoner.Summoner('b')
summoner_middle = Summoner.Summoner('c')
summoner_carry = Summoner.Summoner('Carry_main')
summoner_support = Summoner.Summoner('Support_main')
################

# summoner_doublelift.init_summoner_data()
# summoner_doublelift.init_number_of_matches_by_lane()

summoner_fake_doublelift.number_of_matches_by_lane = {'TOP': 0, 'JUNGLE': 0, 'MIDDLE': 1, 'CARRY': 14, 'SUPPORT': 5}

summoner_top.number_of_matches_by_lane = {'TOP': 34, 'JUNGLE': 27, 'MIDDLE': 25, 'CARRY': 0, 'SUPPORT': 0}
summoner_jungle.number_of_matches_by_lane = {'TOP': 7, 'JUNGLE': 31, 'MIDDLE': 33, 'CARRY': 0, 'SUPPORT': 0}
summoner_middle.number_of_matches_by_lane = {'TOP': 22, 'JUNGLE': 12, 'MIDDLE': 10, 'CARRY': 0, 'SUPPORT': 0}
summoner_carry.number_of_matches_by_lane = {'TOP': 10, 'JUNGLE': 20, 'MIDDLE': 30, 'CARRY': 40, 'SUPPORT': 0}
summoner_support.number_of_matches_by_lane = {'TOP': 0, 'JUNGLE': 10, 'MIDDLE': 20, 'CARRY': 30, 'SUPPORT': 40}
#####################

team_summoners = [summoner_top, summoner_jungle, summoner_middle]

# print(summoner_doublelift.summoner_info)
# TeamComposer.assign_lanes(team_summoners)

versions = Connection.watcher.data_dragon.versions_for_region(Connection.region_v4)
champions_version = versions['n']['champion']

#current_champ_list = Connection.watcher.data_dragon.champions(champions_version)
#print(current_champ_list)
champions = ['Jinx', 'Vi', 'Caitlyn', 'Jayce', 'Viktor']
GoogleTrendAnalyzer.sort_by_popularity(champions)

# champions = Connection.watcher.current_champ_list()
# summoners = []
#
# # if 1 == 1:
#     summoners.append("matchId\tcreateDate\t")
#     for champion in champions['champions']:
#         summoners.append("b chmp " + str(champion['id']) + "\t")
#     for champion in champions['champions']:
#         summoners.append("r chmp " + str(champion['id']) + "\t")
#     summoners.append("winner\n")
#
#     summoners.append("c\t" * 2)
#     summoners.append("c\t" * (2 * len(champions['champions'])))
#     summoners.append("d\n")
#
#     summoners.append("meta\t" * 2)
#     summoners.append("\t" * (2 * len(champions['champions'])))
#     summoners.append("class\n")
# print(champions)
