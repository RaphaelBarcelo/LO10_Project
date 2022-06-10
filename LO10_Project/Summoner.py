import Connection as Connection


class Summoner:

    def __init__(self, summoner_name):
        self.summoner_name = summoner_name
        self.number_of_matches_by_lane = {'TOP': 0, 'JUNGLE': 0, 'MIDDLE': 0, 'CARRY': 0, 'SUPPORT': 0}
        self.match_history = None
        self.ranked_stats = None
        self.summoner_info = None

    def init_summoner_data(self):
        self.summoner_info = Connection.watcher.summoner.by_name(Connection.region_v4, self.summoner_name)
        self.ranked_stats = Connection.watcher.league.by_summoner(Connection.region_v4, self.summoner_info['id'])
        self.match_history = Connection.watcher.match.matchlist_by_puuid(Connection.region_v5,
                                                                         self.summoner_info['puuid'])

    def get_summary(self):
        return {'name': self.summoner_name, 'level': self.summoner_info['summonerLevel'],
                'rank': self.ranked_stats[0]['tier'] + ' ' + self.ranked_stats[0]['rank']}

    #'rank': str(self.ranked_stats[0]['tier'] + ' ' + self.ranked_stats[0]['rank'])}

    def init_number_of_matches_by_lane(self):
        game_number = 0
        for match_id in self.match_history:
            game_number += 1
            match_data = Connection.watcher.match.by_id(Connection.region_v5, match_id)
            match_info = match_data['info']
            for participant in match_info['participants']:
                if participant['puuid'] == self.summoner_info['puuid']:
                    match participant['lane']:
                        case 'TOP':
                            self.number_of_matches_by_lane['TOP'] += 1
                        case 'JUNGLE':
                            self.number_of_matches_by_lane['JUNGLE'] += 1
                        case 'MIDDLE':
                            self.number_of_matches_by_lane['MIDDLE'] += 1
                        case 'BOTTOM':
                            match participant['role']:
                                case 'CARRY':
                                    self.number_of_matches_by_lane['CARRY'] += 1
                                case 'SUPPORT':
                                    self.number_of_matches_by_lane['SUPPORT'] += 1
                        case _:
                            match participant['role']:
                                case 'CARRY':
                                    self.number_of_matches_by_lane['CARRY'] += 1
                                case 'SUPPORT':
                                    self.number_of_matches_by_lane['SUPPORT'] += 1
                                case _:
                                    print('ERROR: lane/role not found')
                                    print('LANE: ' + str(participant['lane']))
                                    print('ROLE: ' + str(participant['role']))
