import Summoner
import TeamComposer as TeamComposer

summoner_doublelift = Summoner.Summoner('Doublelift')

summoner_fake_doublelift = Summoner.Summoner('Doublelift')

summoner_top = Summoner.Summoner('a')
summoner_jungle = Summoner.Summoner('b')
summoner_middle = Summoner.Summoner('c')
summoner_carry = Summoner.Summoner('Carry_main')
summoner_support = Summoner.Summoner('Support_main')
################

#summoner_doublelift.init_summoner_data()
#summoner_doublelift.init_number_of_matches_by_lane()

summoner_fake_doublelift.number_of_matches_by_lane = {'TOP':0, 'JUNGLE':0, 'MIDDLE':1, 'CARRY':14, 'SUPPORT':5}

summoner_top.number_of_matches_by_lane = {'TOP':34, 'JUNGLE':27, 'MIDDLE':25, 'CARRY':0, 'SUPPORT':0}
summoner_jungle.number_of_matches_by_lane = {'TOP':7, 'JUNGLE':31, 'MIDDLE':33, 'CARRY':0, 'SUPPORT':0}
summoner_middle.number_of_matches_by_lane = {'TOP':22, 'JUNGLE':12, 'MIDDLE':10, 'CARRY':0, 'SUPPORT':0}
summoner_carry.number_of_matches_by_lane = {'TOP':10, 'JUNGLE':20, 'MIDDLE':30, 'CARRY':40, 'SUPPORT':0}
summoner_support.number_of_matches_by_lane = {'TOP':0, 'JUNGLE':10, 'MIDDLE':20, 'CARRY':30, 'SUPPORT':40}
#####################

team_summoners = [summoner_top, summoner_jungle, summoner_middle] 

#print(summoner_doublelift.summoner_info)
TeamComposer.assign_lanes(team_summoners)