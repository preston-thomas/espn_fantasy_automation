"""
Preston Thomas
12/09/2025
All source code directly contributed by Preston Thomas
Automation to manage weekly payout notifications.
"""

from espn_api.football import League

class CurrentLeague:

    def __init__(self, league_id: int, year: int, week: int):
        # Not using getters and setters for simplicity as these will not change per object
        self.league_id = league_id
        self.year = year
        self.week = week
        self.league = None
        self.swid = None
        self.espn_s2 = None

    def get_league_id(self) -> int:
        return self.league_id
    
    def get_year(self) -> int:
        return self.year
    
    def get_week(self) -> int:
        return self.week

    def get_league(self) -> League:
        return self.league
    
    def set_league(self, league: League):
        self.league = league

    def set_swid(self, swid: str):
        self.swid = swid

    def get_swid(self) -> str:
        return self.swid
    
    def set_espn_s2(self, s2: str):
        self.espn_s2 = s2

    def get_espn_s2(self) -> str:
        return self.espn_s2

    def initialize_league(self) -> League:
        return League(self.get_league_id(), self.get_year(), espn_s2=self.get_espn_s2(), swid=self.get_swid())
    
    def fetch_current_scores(self, league: League):
        all_matchups = league.scoreboard(self.get_week())
        highest_score = 0

        for matchup in all_matchups:
            print(f"{matchup.home_team.team_name} score: {matchup.home_score}, {matchup.away_team.team_name} score: {matchup.away_score}")
            if matchup.home_score - matchup.away_score < 1 and matchup.home_score - matchup.away_score > 0:
                print(f"Bad beat prize goes to: {matchup.away_team.team_name}")
            elif matchup.away_score - matchup.home_score < 1 and matchup.away_score - matchup.home_score > 0:
                print(f"Bad beat prize goes to: {matchup.home_team.team_name}")
            if matchup.home_score > highest_score:
                highest_score = matchup.home_score
                high_scorer_team = matchup.home_team.team_name
            if matchup.away_score > highest_score:
                highest_score = matchup.away_score
                high_scorer_team = matchup.away_team.team_name
        print(f"Highest point scorer: {high_scorer_team}")

