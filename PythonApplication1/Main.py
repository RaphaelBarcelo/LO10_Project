import Summoner
import TeamComposer as TeamComposer

summoner_doublelift = Summoner.Summoner('Doublelift')

summoner_fake_doublelift = Summoner.Summoner('Doublelift')

summoner_top = Summoner.Summoner('Top_main')
summoner_jungle = Summoner.Summoner('Jungle_main')
summoner_middle = Summoner.Summoner('Middle_main')
summoner_carry = Summoner.Summoner('Carry_main')
summoner_support = Summoner.Summoner('Support_main')
################

#summoner_doublelift.init_summoner_data()
#summoner_doublelift.init_number_of_matches_by_lane()

summoner_fake_doublelift.number_of_matches_by_lane = {'TOP':0, 'JUNGLE':0, 'MIDDLE':1, 'CARRY':14, 'SUPPORT':5}

summoner_top.number_of_matches_by_lane = {'TOP':40, 'JUNGLE':0, 'MIDDLE':10, 'CARRY':20, 'SUPPORT':30}
summoner_jungle.number_of_matches_by_lane = {'TOP':30, 'JUNGLE':40, 'MIDDLE':0, 'CARRY':10, 'SUPPORT':20}
summoner_middle.number_of_matches_by_lane = {'TOP':20, 'JUNGLE':30, 'MIDDLE':40, 'CARRY':0, 'SUPPORT':10}
summoner_carry.number_of_matches_by_lane = {'TOP':10, 'JUNGLE':20, 'MIDDLE':30, 'CARRY':40, 'SUPPORT':0}
summoner_support.number_of_matches_by_lane = {'TOP':0, 'JUNGLE':10, 'MIDDLE':20, 'CARRY':30, 'SUPPORT':40}
#####################

team_summoners = [summoner_top, summoner_jungle, summoner_middle, summoner_fake_doublelift, summoner_support] 

#print(summoner_doublelift.summoner_info)
TeamComposer.assign_lanes(team_summoners)