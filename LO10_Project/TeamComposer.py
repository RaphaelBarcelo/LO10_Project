import Summoner


def assign_lanes(team_summoners):
    summoners_by_lane = {'TOP': [], 'JUNGLE': [], 'MIDDLE': [], 'CARRY': [], 'SUPPORT': []}
    lanes_by_summoner = {}
    lanes_for_each_duplicated_summoner = {}
    team_composition = {'TOP': '', 'JUNGLE': '', 'MIDDLE': '', 'CARRY': '', 'SUPPORT': ''}

    # initialize data
    for lane, summoners in summoners_by_lane.items():
        for summoner in team_summoners:
            summoners.append(summoner)

    # bubble sort to get the best summoners at the top of the list in each lane
    # they are ranked by the number of matches they recently did in each position
    for lane, summoners in summoners_by_lane.items():
        n = len(summoners)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if (summoners[j].number_of_matches_by_lane[lane] < summoners[j + 1].number_of_matches_by_lane[lane]):
                    summoners[j], summoners[j + 1] = summoners[j + 1], summoners[j]

    # get top ranked summoners according to the bubble sort in the team composition
    for lane, summoners in summoners_by_lane.items():
        team_composition[lane] = summoners[0]

    # now we need to get rid of the potential duplicates in the team composition (some people might be assigned to 2 different lanes)
    # we need to assign to these lanes the 2nd best summoner after the one who was duplicated
    # but only when the skill gap is marginal
    # we keep the the duplicated summoner in the lane where the skill gap between him and the second best is significant
    # (there might be multiple duplicated summoners)

    # first we create a reverse dictionary of the team composition dictionary (lane:summoner)
    # to get a dictionary of the lane(s) assigned to each summoner (summoner:lane)
    for key, value in team_composition.items():
        lanes_by_summoner.setdefault(value, set()).add(key)
    lanes_for_each_duplicated_summoner = [values for key, values in lanes_by_summoner.items() if len(values) > 1]

    teamcomp_to_print = 'TEAMCOMP: '
    for lane, summoner in team_composition.items():
        # teamcomp_to_print += lane + ': ' + Summoner.Summoner(summoner).summoner_name + ', '
        teamcomp_to_print += lane
        teamcomp_to_print += ': '
        teamcomp_to_print += summoner.summoner_name
        teamcomp_to_print += ', '
    print(teamcomp_to_print)

    while (lanes_for_each_duplicated_summoner):
        lanes_to_keep = []
        # we iterate over all the lanes that had a duplicated summoner
        for lanes in lanes_for_each_duplicated_summoner:
            maximum_skill_gap = 0
            max_amount_of_matches = -1
            lane_attributed_to_duplicate_summoner = ''
            for lane in lanes:
                # if the numbers of summoners available for a lane is > 1
                if (len(summoners_by_lane[lane]) > 1):
                    current_amount_of_matches = summoners_by_lane[lane][0].number_of_matches_by_lane[lane]
                    current_skill_gap = current_amount_of_matches - \
                                        summoners_by_lane[lane][1].number_of_matches_by_lane[lane]
                    # if the skill gap between the summoner duplicated and the second summoner available for a given lane
                    # is the worst, the duplicated summoner is assigned this lane
                    if (current_skill_gap > maximum_skill_gap):
                        maximum_skill_gap = current_skill_gap
                        max_amount_of_matches = current_amount_of_matches
                        lane_attributed_to_duplicate_summoner = lane
                    else:
                        # if the skill gap is the same but the duplicated summoner is better in the lane being iterrated
                        # he is assigned to this lane
                        if (
                                current_skill_gap == maximum_skill_gap and max_amount_of_matches > -1 and current_amount_of_matches > max_amount_of_matches):
                            maximum_skill_gap = current_skill_gap
                            max_amount_of_matches = current_amount_of_matches
                            lane_attributed_to_duplicate_summoner = lane
            lanes_to_keep.append(lane_attributed_to_duplicate_summoner)

        # in all the lanes that have a duplicate, we delete the summoner in first position (the duplicate)
        # leaving room for the summoner in second position
        for lanes in lanes_for_each_duplicated_summoner:
            for lane in lanes:
                # we let the duplicated summoner keep the lanes he was assigned to
                if (lane not in lanes_to_keep):
                    del summoners_by_lane[lane][0]
                    if (not summoners_by_lane[lane]):
                        del team_composition[lane]
                        del summoners_by_lane[lane]

        # reassign the top summoners to each lane
        for lane, summoners in summoners_by_lane.items():
            team_composition[lane] = summoners[0]

        # check again for duplicates
        lanes_by_summoner.clear()
        lanes_for_each_duplicated_summoner.clear()
        for key, value in team_composition.items():
            lanes_by_summoner.setdefault(value, set()).add(key)
            lanes_for_each_duplicated_summoner = [values for key, values in lanes_by_summoner.items() if
                                                  len(values) > 1]

        teamcomp_to_print = 'TEAMCOMP: '
        for lane, summoner in team_composition.items():
            # teamcomp_to_print += lane + ': ' + Summoner.Summoner(summoner).summoner_name + ', '
            teamcomp_to_print += lane
            teamcomp_to_print += ': '
            teamcomp_to_print += summoner.summoner_name
            teamcomp_to_print += ', '
        print(teamcomp_to_print)
