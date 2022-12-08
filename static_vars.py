
# This file is just for project organization. It has various structures of long strings that
# are displayed in the program

create_fantasy_table = """
                   CREATE TABLE "fantasy" (
                        "name"	TEXT,
                        "club"	TEXT,
                        "goals"	INTEGER,
                        "assists"	INTEGER,
                        "total_points"	INTEGER,
                        "minutes"	INTEGER,
                        "saves"	INTEGER,
                        "conceded"	INTEGER,
                        "creativity"	REAL,
                        "influence"	REAL,
                        "threat"	INTEGER,
                        "bonus"	INTEGER,
                        "BPS"	INTEGER,
                        "ICT_index"	REAL,
                        "clean_sheets"	INTEGER,
                        "reds"	INTEGER,
                        "yellows"	INTEGER,
                        "position"	TEXT
                    )
                   """
                   
create_players_table = """
                   CREATE TABLE "players" (
                        "name"	TEXT,
                        "club"	TEXT,
                        "nationality"	TEXT,
                        "position"	TEXT,
                        "age"	INTEGER,
                        "matches"	INTEGER,
                        "starts"	INTEGER,
                        "minutes"	INTEGER,
                        "goals"	INTEGER,
                        "assists"	INTEGER,
                        "passes_attempted"	INTEGER,
                        "perc_passes_completed"	REAL,
                        "pen_goals"	INTEGER,
                        "pens_attempted"	INTEGER,
                        "xG"	REAL,
                        "xA"	REAL,
                        "yellows"	INTEGER,
                        "reds"	INTEGERa
                    )
                   """
                   
create_season_table = """
                   CREATE TABLE "season" (
                        "game_id"	INTEGER,
                        "date"	TEXT,
                        "time"	TEXT,
                        "home_team"	TEXT,
                        "away_team"	TEXT,
                        "ft_home_goals"	INTEGER,
                        "ft_away_goals"	INTEGER,
                        "ft_result"	TEXT,
                        "ht_home_goals"	INTEGER,
                        "ht_away_goals"	INTEGER,
                        "ht_result"	TEXT,
                        "referee"	TEXT,
                        "home_shots"	INTEGER,
                        "away_shots"	INTEGER,
                        "home_shots_ot"	INTEGER,
                        "away_shots_ot"	INTEGER,
                        "home_fouls"	INTEGER,
                        "away_fouls"	INTEGER,
                        "home_corners"	INTEGER,
                        "away_corners"	INTEGER,
                        "home_yellows"	INTEGER,
                        "away_yellows"	INTEGER,
                        "home_reds"	INTEGER,
                        "away_reds"	INTEGER
                    )
                   """

introduction = """
This interface allows you view various statistics regarding
the Barclay's Premier League 2020-2021 season. It utilizes
data on the season itself, the players, and also the official
Fantasy Premier League game during the 2020-2021 season.
               """

season_columns_descriptions = [
    "[INTEGER] unique id for the match",
    "[TEXT] date of the match",
    "[TEXT] time of the match",
    "[TEXT] home team for the match",
    "[TEXT] away team for the match",
    "[INTEGER] goals scored by the home team by full-time",
    "[INTEGER] goals scored by the away team by full-time",
    "[TEXT] who won ('H'-home or 'A'-away or 'D'-draw)",
    "[INTEGER] goals scored by the home team by half-time",
    "[INTEGER] goals scored by the away team by half-time",
    "[TEXT] who was winning at half-time ('H'-home or 'A'-away or 'D'-draw)",
    "[TEXT] the referee of the match",
    "[INTEGER] number of shots by home team",
    "[INTEGER] number of shots by away team",
    "[INTEGER] number of shots on target by the home team",
    "[INTEGER] number of shots on target by the away team",
    "[INTEGER] number of fouls committed by the home team",
    "[INTEGER] number of fouls committed by the away team",
    "[INTEGER] number of corners awarded to the home team",
    "[INTEGER] number of corners awarded to the away team",
    "[INTEGER] number of yellow cards given to the home team",
    "[INTEGER] number of yellow cards given to the away team",
    "[INTEGER] number of red cards given to the home team",
    "[INTEGER] number of red cards given to the away team"
]

fantasy_columns_descriptions = [
    "[TEXT] full name of the player",
    "[INTEGER] total points accumulated by the player",
    "[INTEGER] total saves made by the player",
    "[INTEGER] total goals conceded while this player was on the pitch",
    "[REAL] in-game metric comparing the player's creativity to others in the league",
    "[REAL] in-game metric comparing the player's influence on the game to others in the league",
    "[INTEGER] in-game metric comparing the player's threat toward the opposition goal to others in the league",
    "[INTEGER] the total extra points awarded to players who were the best in a given match",
    "[INTEGER] score calculated by an in-game algorithm to determine who earns bonus points in a match",
    "[REAL] a (scaled) combined score of the influence, creativity, and threat metrics",
    "[INTEGER] total clean sheets earned by the player",
    "[TEXT] the position the player is in the game"
]

players_columns_descriptions = [
    "[TEXT] full name of the player",
    "[TEXT] the club the player plays for",
    "[TEXT] the player's nationality",
    "[TEXT] the position(s) the player plays in",
    "[INTEGER] the player's age",
    "[INTEGER] the number of matches the player played in",
    "[INTEGER] the number of starts the player had",
    "[INTEGER] the total number of minutes played by the player",
    "[INTEGER] the number of goals scored by the player",
    "[INTEGER] the number of assists made by the player",
    "[INTEGER] total number of passes the player attempted",
    "[REAL] the player's successful pass percentage",
    "[INTEGER] the number of penalty goals scored",
    "[INTEGER] the number of penalties attempted",
    "[REAL] official league metric measuring the player's expected goals based on their chances",
    "[REAL] official league metric measuring the player's expected assists based on their chances created",
    "[INTEGER] total number of yellow cards accumulated by the player",
    "[INTEGER] total number of red cards accumulated by the player",
]
