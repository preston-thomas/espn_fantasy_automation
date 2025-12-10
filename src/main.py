"""
Preston Thomas
12/09/2025
All source code directly contributed by Preston Thomas
Automation to manage weekly payout notifications.
"""

import league
import os
import dotenv

def main():
    # Load private data from .env file
    dotenv.load_dotenv()

    entered_year = int(input(f"Please enter the year.\n"))
    entered_week = int(input(f"Please enter the week.\n"))
    home_league = league.CurrentLeague(os.environ.get("HOME_LEAGUE_ID"), entered_year, entered_week)
    home_league.set_espn_s2(os.environ.get("ESPN_S2"))
    home_league.set_swid(os.environ.get("ESPN_SWID"))
    home_league.set_league(home_league.initialize_league())
    home_league.fetch_current_scores(home_league.get_league())

if __name__ == '__main__':
    main()