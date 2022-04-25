import Summoner as Summoner
from itertools import chain

def assign_lanes(team_summoners):
    
    summoners_by_lane = {'TOP':[], 'JUNGLE':[], 'MIDDLE':[], 'CARRY':[], 'SUPPORT':[]}
    lanes_by_summoner = {}
    lanes_for_each_duplicated_summoner = {}
    #team_composition = {'TOP':'', 'JUNGLE':'', 'MIDDLE':'', 'CARRY':'', 'SUPPORT':''}
    team_composition = {}

   #initiate data
    for lane, summoners in summoners_by_lane.items():
        for summoner in team_summoners:
            summoners.append(summoner)

   #bubble sort 
    for lane, summoners in summoners_by_lane.items():
        n = len(summoners)
        # Traverse through all array elements
        for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if (summoners[j].number_of_matches_by_lane[lane] < summoners[j + 1].number_of_matches_by_lane[lane]) :
                    summoners[j], summoners[j + 1] = summoners[j + 1], summoners[j]
    
    for lane, summoners in summoners_by_lane.items():
        team_composition[lane]=summoners[0]
    
    for key, value in team_composition.items():
        lanes_by_summoner.setdefault(value, set()).add(key)
    lanes_for_each_duplicated_summoner = [values for key, values in lanes_by_summoner.items() if len(values) > 1]

    for lanes in lanes_for_each_duplicated_summoner:
        print('\n')
        print('___________________________')
        print('\n')
        for lane in lanes:
            print('\n')
            print('OWOOOOOOOOOOOOOOOOOOOOOO')
            print(str(lane) + ': ' + str(summoner.summoner_name.encode().decode()))
            print('\n')
            
    ### ### ##
    #remove duplicates
    ### ### ##
    #while(len(lanes_for_each_duplicated_summoner)>1):
    i = 20
    while(i < 10):
        lanes_to_keep = []
        for lanes in lanes_for_each_duplicated_summoner:
            maximum_skill_gap = 0
            lane_attributed_to_duplicate_summoner = ''
            for lane in lanes:
                if(len(summoners_by_lane[lane])>1):
                    current_skill_gap = summoners_by_lane[lane][0].number_of_matches_by_lane[lane] - summoners_by_lane[lane][1].number_of_matches_by_lane[lane]
                    if (current_skill_gap > maximum_skill_gap):
                        lane_attributed_to_duplicate_summoner = lane
                        maximum_skill_gap = current_skill_gap
            lanes_to_keep.append(lane_attributed_to_duplicate_summoner)
    
        for lanes in lanes_for_each_duplicated_summoner:
            for lane in lanes:
                if (lane not in lanes_to_keep):
                    del summoners_by_lane[lane][0]
                    if(len(summoners_by_lane[lane]) == 0):
                        summoners_by_lane[lane].append('')
    
        for lane, summoners in summoners_by_lane.items():
            team_composition[lane]=summoners[0]
    
        for key, value in team_composition.items():
            lanes_by_summoner.setdefault(value, set()).add(key)
            lanes_for_each_duplicated_summoner = [values for key, values in lanes_by_summoner.items() if len(values) > 1]

        print(i)
        for lane, summoner in team_composition.items():
            print('\n')
            print(str(lane) + ': ' + str(summoner.summoner_name.encode().decode()))
            print('\n')

        i += 1
     
    for lane, summoner in team_composition.items():
        print('\n')
        #print(str(lane) + ': ' + str(summoner.summoner_name))
        print('\n')