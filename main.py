
import sqlite3 as sql
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pwinput

import static_vars as sv

def main():
    try:
        conn, cursor = establish_db_connection()
    except ConnectionError:
        print("\nConnection to database failed.")
    finally:
        print("\nWelcome!")
        
    print(sv.introduction)
    
    print("What would you like to do?")
    print("  a) Summary Statistics\n  b) Standard Query\n"
          "  c) Data Visualizations\n  d) Edit Data (password required)")
    
    choice = input("  > ")
    while choice not in ['a', 'b', 'c', 'd']:
        print("\nInvalid choice. Choose again:")
        choice = input("  > ")
    
    match choice:
        # summary statistics
        # ----------------------------
        case 'a':
            print("\nYou chose to view summary statistics.")
            print("To get a statistic, type your desired table, attribute,"
                  " and measurement when prompted.")
            
            print("\nYour table options:\n  - fantasy\n  - players\n  - season")
            table_choice = input("  > ")
            while table_choice not in ["fantasy", "players", "season"]:
                print("\nInvalid table name. Choose again:")
                table_choice = input("  > ")
            
            match table_choice:
                case "fantasy":
                    queried_fantasy_columns = cursor.execute(f"""
                                                            PRAGMA table_info("fantasy");
                                                            """).fetchall()
                    fantasy_columns = []
                    valid_fantasy_columns = []
                    for i in range(len(queried_fantasy_columns)):
                        fantasy_columns.append(queried_fantasy_columns[i][1])
                        
                    print(f"\nYour column options for the {table_choice} table (must be an INTEGER or REAL type):")
                    for i in range(len(fantasy_columns)):
                        if sv.fantasy_columns_descriptions[i].__contains__("INTEGER") or\
                           sv.fantasy_columns_descriptions[i].__contains__("REAL"):
                            print(f"{fantasy_columns[i] : >12} :  {sv.fantasy_columns_descriptions[i]}")
                            valid_fantasy_columns.append(fantasy_columns[i])
                        
                    column_choice = input("  > ")
                    while column_choice not in valid_fantasy_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nYour measurement options:\n  - avg\n  - min\n  - max\n  - sum")
                    
                    measurement_choice = input("  > ")
                    while measurement_choice not in ["avg", "min", "max", "sum"]:
                        print("\nInvalid measurement. Choose again:")
                        measurement_choice = input("  > ")
                    
                    summary_stats(cursor, table_choice, column_choice, measurement_choice)
                
                case "players":
                    queried_players_columns = cursor.execute(f"""
                                                            PRAGMA table_info("players");
                                                            """).fetchall()
                    players_columns = []
                    valid_players_columns = []
                    for i in range(len(queried_players_columns)):
                        players_columns.append(queried_players_columns[i][1])
                        
                    print(f"\nYour column options for the {table_choice} table (must be an INTEGER or REAL type):")
                    for i in range(len(players_columns)):
                        if sv.players_columns_descriptions[i].__contains__("INTEGER") or\
                           sv.players_columns_descriptions[i].__contains__("REAL"):
                            print(f"{players_columns[i] : >21} :  {sv.players_columns_descriptions[i]}")
                            valid_players_columns.append(players_columns[i])
                        
                    column_choice = input("  > ")
                    while column_choice not in valid_players_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nYour measurement options:\n  - avg\n  - min\n  - max\n  - sum")
                    
                    measurement_choice = input("  > ")
                    while measurement_choice not in ["avg", "min", "max", "sum"]:
                        print("\nInvalid measurement. Choose again:")
                        measurement_choice = input("  > ")
                    
                    summary_stats(cursor, table_choice, column_choice, measurement_choice)
                
                case "season":
                    queried_season_columns = cursor.execute(f"""
                                                            PRAGMA table_info("season");
                                                            """).fetchall()
                    season_columns = []
                    valid_season_columns = []
                    for i in range(len(queried_season_columns)):
                        season_columns.append(queried_season_columns[i][1])
                        
                    print(f"\nYour column options for the {table_choice} table (must be an INTEGER type):")
                    for i in range(len(season_columns)):
                        if sv.season_columns_descriptions[i].__contains__("INTEGER"):
                            print(f"{season_columns[i] : >18} :  {sv.season_columns_descriptions[i]}")
                            valid_season_columns.append(season_columns[i])
                        
                    column_choice = input("  > ")
                    while column_choice not in valid_season_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nYour measurement options:\n  - avg\n  - min\n  - max\n  - sum")
                    
                    measurement_choice = input("  > ")
                    while measurement_choice not in ["avg", "min", "max", "sum"]:
                        print("\nInvalid measurement. Choose again:")
                        measurement_choice = input("  > ")
                    
                    summary_stats(cursor, table_choice, column_choice, measurement_choice)
                    
            
        # Standard Query
        # ----------------------------
        case 'b':
            print("\nYou chose to make a standard query.")
            print("You can choose to make query that involves a join between two tables,\n"
                  "or you can query to just one table.")
            print("\nYour table options:\n  - fantasy\n  - players\n  - season\n  - join")
            table_choice = input("  > ")
            while table_choice not in ["fantasy", "players", "season", "join"]:
                print("\nInvalid choice name. Choose again:")
                table_choice = input("  > ")
            
            match table_choice:
                case "fantasy":
                    queried_fantasy_columns = cursor.execute(f"""
                                                            PRAGMA table_info("fantasy");
                                                            """).fetchall()
                    fantasy_columns = []
                    for i in range(len(queried_fantasy_columns)):
                        fantasy_columns.append(queried_fantasy_columns[i][1])
                        
                    print(f"\nYour column options for the {table_choice}:")
                    for i in range(len(fantasy_columns)):
                        print(f"{fantasy_columns[i] : >12} :  {sv.fantasy_columns_descriptions[i]}")
                        
                    column_choice = input("  > ")
                    while column_choice not in fantasy_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nBuild your WHERE clause.")
                    print("Enter the column you'd like to filter by:")
                    filter_column = input("WHERE ")
                    while filter_column not in fantasy_columns:
                        print("\nInvalid column name. Choose again:")
                        filter_column = input("WHERE ")
                    
                    print("Enter the comparison operator (<, >, =):")
                    comparison_operator = input(f"WHERE {filter_column}")
                    while comparison_operator not in ['<', '>', '=']:
                        print("Invalid comparison operator. Choose again: ")
                        comparison_operator = input(f"WHERE {filter_column}")
                        
                    print("Enter the value to filter by: ")
                    filter_value = input(f"WHERE {filter_column}{comparison_operator}")
                    
                    where_clause = f"WHERE {filter_column}{comparison_operator}'{filter_value}'"
                    
                    again = True
                    while again:
                        print("\nWould you like to add to the WHERE clause? (y/n):")
                        again_choice = input("  > ")
                        while again_choice not in ['y', 'n']:
                            print("\nInvalid input. Choose again:")
                            again_choice = input("  > ")
                        
                        if again_choice == 'n':
                            again = False
                        else:
                            print("Which conjunction? (AND, OR):")
                            conjunction = input("... ")
                            while conjunction not in ['AND', 'OR']:
                                print("\nInvalid input. Choose again:")
                                conjunction = input("... ")
                                
                            print("Enter the column you'd like to filter by:")
                            filter_column = input(f"...{conjunction} WHERE ")
                            while filter_column not in fantasy_columns:
                                print("\nInvalid column name. Choose again:")
                                filter_column = input(f"...{conjunction} WHERE ")
                            
                            print("Enter the comparison operator (<, >, =):")
                            comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                            while comparison_operator not in ['<', '>', '=']:
                                print("Invalid comparison operator. Choose again: ")
                                comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                                
                            print("Enter the value to filter by: ")
                            filter_value = input(f"...{conjunction} WHERE {filter_column}{comparison_operator}")
                            
                            where_clause += f" {conjunction} {filter_column}{comparison_operator}'{filter_value}'"
                    
                    standard_query(cursor, table_choice, column_choice, where_clause, False)
                    
                case "players":
                    queried_players_columns = cursor.execute(f"""
                                                            PRAGMA table_info("players");
                                                            """).fetchall()
                    players_columns = []
                    for i in range(len(queried_players_columns)):
                        players_columns.append(queried_players_columns[i][1])
                        
                    print(f"\nYour column options for the {table_choice}:")
                    for i in range(len(players_columns)):
                        print(f"{players_columns[i] : >21} :  {sv.players_columns_descriptions[i]}")
                        
                    column_choice = input("  > ")
                    while column_choice not in players_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nBuild your WHERE clause.")
                    print("Enter the column you'd like to filter by:")
                    filter_column = input("WHERE ")
                    while filter_column not in players_columns:
                        print("\nInvalid column name. Choose again:")
                        filter_column = input("WHERE ")
                    
                    print("Enter the comparison operator (<, >, =):")
                    comparison_operator = input(f"WHERE {filter_column}")
                    while comparison_operator not in ['<', '>', '=']:
                        print("Invalid comparison operator. Choose again: ")
                        comparison_operator = input(f"WHERE {filter_column}")
                        
                    print("Enter the value to filter by: ")
                    filter_value = input(f"WHERE {filter_column}{comparison_operator}")
                    
                    where_clause = f"WHERE {filter_column}{comparison_operator}'{filter_value}'"
                    
                    again = True
                    while again:
                        print("\nWould you like to add to the WHERE clause? (y/n):")
                        again_choice = input("  > ")
                        while again_choice not in ['y', 'n']:
                            print("\nInvalid input. Choose again:")
                            again_choice = input("  > ")
                        
                        if again_choice == 'n':
                            again = False
                        else:
                            print("Which conjunction? (AND, OR):")
                            conjunction = input("... ")
                            while conjunction not in ['AND', 'OR']:
                                print("\nInvalid input. Choose again:")
                                conjunction = input("... ")
                                
                            print("Enter the column you'd like to filter by:")
                            filter_column = input(f"...{conjunction} WHERE ")
                            while filter_column not in players_columns:
                                print("\nInvalid column name. Choose again:")
                                filter_column = input(f"...{conjunction} WHERE ")
                            
                            print("Enter the comparison operator (<, >, =):")
                            comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                            while comparison_operator not in ['<', '>', '=']:
                                print("Invalid comparison operator. Choose again: ")
                                comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                                
                            print("Enter the value to filter by: ")
                            filter_value = input(f"...{conjunction} WHERE {filter_column}{comparison_operator}")
                            
                            where_clause += f" {conjunction} {filter_column}{comparison_operator}'{filter_value}'"
                    
                    standard_query(cursor, table_choice, column_choice, where_clause, False)
                
                case "season":
                    queried_season_columns = cursor.execute(f"""
                                                            PRAGMA table_info("season");
                                                            """).fetchall()
                    season_columns = []
                    for i in range(len(queried_season_columns)):
                        season_columns.append(queried_season_columns[i][1])
                        
                    print(f"\nYour column options for the {table_choice}:")
                    for i in range(len(season_columns)):
                        print(f"{season_columns[i] : >13} :  {sv.season_columns_descriptions[i]}")
                        
                    column_choice = input("  > ")
                    while column_choice not in season_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nBuild your WHERE clause.")
                    print("Enter the column you'd like to filter by:")
                    filter_column = input("WHERE ")
                    while filter_column not in season_columns:
                        print("\nInvalid column name. Choose again:")
                        filter_column = input("WHERE ")
                    
                    print("Enter the comparison operator (<, >, =):")
                    comparison_operator = input(f"WHERE {filter_column}")
                    while comparison_operator not in ['<', '>', '=']:
                        print("Invalid comparison operator. Choose again: ")
                        comparison_operator = input(f"WHERE {filter_column}")
                        
                    print("Enter the value to filter by: ")
                    filter_value = input(f"WHERE {filter_column}{comparison_operator}")
                    
                    where_clause = f"WHERE {filter_column}{comparison_operator}'{filter_value}'"
                    
                    again = True
                    while again:
                        print("\nWould you like to add to the WHERE clause? (y/n):")
                        again_choice = input("  > ")
                        while again_choice not in ['y', 'n']:
                            print("\nInvalid input. Choose again:")
                            again_choice = input("  > ")
                        
                        if again_choice == 'n':
                            again = False
                        else:
                            print("Which conjunction? (AND, OR):")
                            conjunction = input("... ")
                            while conjunction not in ['AND', 'OR']:
                                print("\nInvalid input. Choose again:")
                                conjunction = input("... ")
                                
                            print("Enter the column you'd like to filter by:")
                            filter_column = input(f"...{conjunction} WHERE ")
                            while filter_column not in season_columns:
                                print("\nInvalid column name. Choose again:")
                                filter_column = input(f"...{conjunction} WHERE ")
                            
                            print("Enter the comparison operator (<, >, =):")
                            comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                            while comparison_operator not in ['<', '>', '=']:
                                print("Invalid comparison operator. Choose again: ")
                                comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                                
                            print("Enter the value to filter by: ")
                            filter_value = input(f"...{conjunction} WHERE {filter_column}{comparison_operator}")
                            
                            where_clause += f" {conjunction} {filter_column}{comparison_operator}'{filter_value}'"
                    
                    standard_query(cursor, table_choice, column_choice, where_clause, False)
                
                case "join":
                    print("\nYou will join the Fantasy and Players tables.")
                    queried_fantasy_columns = cursor.execute(f"""
                                                            PRAGMA table_info("fantasy");
                                                            """).fetchall()
                    fantasy_columns = []
                    for i in range(len(queried_fantasy_columns)):
                        fantasy_columns.append(queried_fantasy_columns[i][1])
                        
                    queried_players_columns = cursor.execute(f"""
                                                            PRAGMA table_info("players");
                                                            """).fetchall()
                    players_columns = []
                    for i in range(len(queried_players_columns)):
                        if queried_players_columns != "name":
                            players_columns.append(queried_players_columns[i][1])
                    
                    combined_columns = fantasy_columns + players_columns
                    combined_descriptions = sv.fantasy_columns_descriptions + sv.players_columns_descriptions
                        
                    print(f"\nYour column options for the {table_choice}:")
                    for i in range(len(combined_columns)):
                        print(f"{combined_columns[i] : >21} :  {combined_descriptions[i]}")
                        
                    column_choice = input("  > ")
                    while column_choice not in combined_columns:
                        print("\nInvalid column name. Choose again:")
                        column_choice = input("  > ")
                    
                    print("\nBuild your WHERE clause.")
                    print("Enter the column you'd like to filter by:")
                    filter_column = input("WHERE ")
                    while filter_column not in combined_columns:
                        print("\nInvalid column name. Choose again:")
                        filter_column = input("WHERE ")
                    
                    print("Enter the comparison operator (<, >, =):")
                    comparison_operator = input(f"WHERE {filter_column}")
                    while comparison_operator not in ['<', '>', '=']:
                        print("Invalid comparison operator. Choose again: ")
                        comparison_operator = input(f"WHERE {filter_column}")
                        
                    print("Enter the value to filter by: ")
                    filter_value = input(f"WHERE {filter_column}{comparison_operator}")
                    
                    where_clause = f"WHERE {filter_column}{comparison_operator}'{filter_value}'"
                    
                    again = True
                    while again:
                        print("\nWould you like to add to the WHERE clause? (y/n):")
                        again_choice = input("  > ")
                        while again_choice not in ['y', 'n']:
                            print("\nInvalid input. Choose again:")
                            again_choice = input("  > ")
                        
                        if again_choice == 'n':
                            again = False
                        else:
                            print("Which conjunction? (AND, OR):")
                            conjunction = input("... ")
                            while conjunction not in ['AND', 'OR']:
                                print("\nInvalid input. Choose again:")
                                conjunction = input("... ")
                                
                            print("Enter the column you'd like to filter by:")
                            filter_column = input(f"...{conjunction} WHERE ")
                            while filter_column not in season_columns:
                                print("\nInvalid column name. Choose again:")
                                filter_column = input(f"...{conjunction} WHERE ")
                            
                            print("Enter the comparison operator (<, >, =):")
                            comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                            while comparison_operator not in ['<', '>', '=']:
                                print("Invalid comparison operator. Choose again: ")
                                comparison_operator = input(f"...{conjunction} WHERE {filter_column}")
                                
                            print("Enter the value to filter by: ")
                            filter_value = input(f"...{conjunction} WHERE {filter_column}{comparison_operator}")
                            
                            where_clause += f" {conjunction} {filter_column}{comparison_operator}'{filter_value}'"
                    
                    standard_query(cursor, "fantasy", column_choice, where_clause, True)
                    
                    
            
        # Visualizations
        # ----------------------------
        # c) Allow visualizations for key metrics of your choice with at least two different types of plots.
            # show two visualizations for each
        case 'c':
            print("\nYou chose to see the data displayed in graphs.")
            
            print("Which graph would you like to view?\n  - players bar chart\n  - season summary")
            graph_choice = input("  > ")
            while graph_choice not in ["players bar chart", "season summary"]:
                print("\nInvalid graph choice. Choose again:")
                graph_choice = input("  > ")
            
            graph(cursor, graph_choice)
            
        
        # Edit Database    
        # ---------------------------- 
        # d) App should allow user to add, remove, and modify records from all tables.
            # allow edits to fantasy only
        case "d":
            print("\nYou chose to edit the data.")
            edit_database(conn, cursor)


    conn.close()
            

def establish_db_connection():
    """
    Function to create the database and populate the tables using the csv files
    """
    # create a connection to the database
    conn = sql.connect("pl-data/premier-league-20-21.db")
    cursor = conn.cursor()
    
    # ensure no tables exist in the database
    cursor.execute("DROP TABLE IF EXISTS fantasy;")
    cursor.execute("DROP TABLE IF EXISTS players;")
    cursor.execute("DROP TABLE IF EXISTS season;")

    # create empty tables in the database
    cursor.execute(sv.create_fantasy_table)
    cursor.execute(sv.create_players_table)
    cursor.execute(sv.create_season_table)

    # read the data into dataframes
    fantasy = pd.read_csv("pl-data/fantasy.csv")
    players = pd.read_csv("pl-data/players.csv")
    season = pd.read_csv("pl-data/season.csv")

    # transfer the dataframes into the database as separate tables
    fantasy.to_sql("fantasy", conn, if_exists="replace", index=False, index_label=None)
    players.to_sql("players", conn, if_exists="replace", index=False, index_label=None)
    season.to_sql("season", conn, if_exists="replace", index=False, index_label=None)

    # commit the changes made and then close the connection to the database
    conn.commit()
    
    return conn, cursor
    

def summary_stats(cursor, table, column, measurement):
    # retrieve desired data, calculate, and return the statistic
    queried_statistic = cursor.execute(f"""
                                       SELECT {measurement}({column})
                                       FROM {table};
                                       """).fetchall()
    queried_statistic = queried_statistic[0][0]
    
    print(f"\n<-- The {measurement} of {column} in the {table} table is {round(queried_statistic, 3)} -->\n")


def standard_query(cursor, table, column, where_clause, is_join):
    # used to query a specific value from the database based on user input
    if not is_join:
        queried_statistic = cursor.execute(f"""
                                            SELECT {column}
                                            FROM {table}
                                            {where_clause};
                                            """).fetchall()
        if len(queried_statistic) > 0:
            print("\n---")
            for tup in queried_statistic:
                print(f"  {tup[0]}")
            print("---")
        else:
            print("\n---\n  no data exists for this query\n---\n")
                
    else:
        queried_statistic = cursor.execute(f"""
                                            SELECT {column}
                                            FROM fantasy
                                            INNER JOIN players
                                            ON fantasy.name = players.name
                                            {where_clause};
                                            """).fetchall()
        if len(queried_statistic) > 0:
            print("\n---")
            for tup in queried_statistic:
                print(f"  {tup[0]}")
            print("---")
        else:
            print("\n---\n  no data exists for this query\n---\n")


def graph(cursor, choice):
    # plot the data and display the graph
    if choice == "players bar chart":
        positions = ["GK", "DEF", "MID", "FWD"]
        
        for pos in positions:
            queried_data = cursor.execute(f"""
                                        SELECT avg(matches), avg(goals), avg(assists)
                                        FROM players
                                        WHERE position='{pos}';
                                        """).fetchall()
            
            for (matches, goals, assists) in queried_data:
                match pos:
                    case "GK":
                        goalkeeper_avgs = [matches, goals, assists]
                    case "DEF":
                        defender_avgs = [matches, goals, assists]
                    case "MID":
                        midfielder_avgs = [matches, goals, assists]
                    case "FWD":
                        forward_avgs = [matches, goals, assists]
        
        measurements = ["Matches", "Goals", "Assists"]

        width = 0.2
        x_gk = [x - 1.5*width for x in range(len(goalkeeper_avgs))]
        x_def = [x - width/2 for x in range(len(defender_avgs))]
        x_mid = [x + width/2 for x in range(len(midfielder_avgs))]
        x_fwd = [x + 1.5*width for x in range(len(forward_avgs))]
        
        x = np.arange(len(measurements))
        fig, ax = plt.subplots()
        
        ax.bar(x_gk, goalkeeper_avgs, width, label="Goalkeepers", color="maroon", edgecolor="sienna")
        ax.bar(x_def, defender_avgs, width, label="Defenders", color="firebrick", edgecolor="sienna")
        ax.bar(x_mid, midfielder_avgs, width, label="Midfielders", color="lightcoral", edgecolor="sienna")
        ax.bar(x_fwd, forward_avgs, width, label="Forwards", color="mistyrose", edgecolor="sienna")
        
        ax.set_title("Average Player Statistics By Position")
        ax.set_facecolor("gainsboro")
        ax.set_xticks(x, measurements)
        ax.set_ylabel("Average Value")
        ax.legend()

        fig.set_figwidth(20)
        fig.set_figheight(10)
        fig.tight_layout()
        
        plt.yticks([num for num in range(0, 31)])
        
        plt.show()
        
    else:
        gw = [
            0, 1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17,
            18, 19, 20, 21, 22,
            23, 24, 25, 26, 27,
            28, 29, 30, 31, 32,
            33, 34, 35, 36, 37, 38
            ]
        
        ars = [0]
        avl = [0]
        bha = [0]
        bur = [0]
        che = [0]
        cry = [0]
        eve = [0]
        ful = [0]
        lee = [0]
        lei = [0]
        liv = [0]
        mci = [0]
        mun = [0]
        new = [0]
        shu = [0]
        sou = [0]
        tot = [0]
        wba = [0]
        whu = [0]
        wol = [0]
        
        queried_data = cursor.execute(f"""
                                        SELECT home_team, away_team, ft_result
                                        FROM season;
                                        """).fetchall()
        for (ht, at, r) in queried_data:
            match r:
                case 'H':
                    match ht:
                        case "Arsenal":
                            curr_points = ars[-1]
                            new_points = curr_points + 3
                            ars.append(new_points)
                        case "Aston Villa":
                            curr_points = avl[-1]
                            new_points = curr_points + 3
                            avl.append(new_points)
                        case "Brighton":
                            curr_points = bha[-1]
                            new_points = curr_points + 3
                            bha.append(new_points)
                        case "Burnley":
                            curr_points = bur[-1]
                            new_points = curr_points + 3
                            bur.append(new_points)
                        case "Chelsea":
                            curr_points = che[-1]
                            new_points = curr_points + 3
                            che.append(new_points)
                        case "Crystal Palace":
                            curr_points = cry[-1]
                            new_points = curr_points + 3
                            cry.append(new_points)
                        case "Everton":
                            curr_points = eve[-1]
                            new_points = curr_points + 3
                            eve.append(new_points)
                        case "Fulham":
                            curr_points = ful[-1]
                            new_points = curr_points + 3
                            ful.append(new_points)
                        case "Leeds United":
                            curr_points = lee[-1]
                            new_points = curr_points + 3
                            lee.append(new_points)
                        case "Leicester City":
                            curr_points = lei[-1]
                            new_points = curr_points + 3
                            lei.append(new_points)
                        case "Liverpool":
                            curr_points = liv[-1]
                            new_points = curr_points + 3
                            liv.append(new_points)
                        case "Manchester City":
                            curr_points = mci[-1]
                            new_points = curr_points + 3
                            mci.append(new_points)
                        case "Manchester United":
                            curr_points = mun[-1]
                            new_points = curr_points + 3
                            mun.append(new_points)
                        case "Newcastle United":
                            curr_points = new[-1]
                            new_points = curr_points + 3
                            new.append(new_points)
                        case "Sheffield United":
                            curr_points = shu[-1]
                            new_points = curr_points + 3
                            shu.append(new_points)
                        case "Southampton":
                            curr_points = sou[-1]
                            new_points = curr_points + 3
                            sou.append(new_points)
                        case "Tottenham Hotspur":
                            curr_points = tot[-1]
                            new_points = curr_points + 3
                            tot.append(new_points)
                        case "West Bromwich Albion":
                            curr_points = wba[-1]
                            new_points = curr_points + 3
                            wba.append(new_points)
                        case "West Ham United":
                            curr_points = whu[-1]
                            new_points = curr_points + 3
                            whu.append(new_points)
                        case "Wolverhampton Wanderers":
                            curr_points = wol[-1]
                            new_points = curr_points + 3
                            wol.append(new_points)
                    match at:
                        case "Arsenal":
                            curr_points = ars[-1]
                            new_points = curr_points + 0
                            ars.append(new_points)
                        case "Aston Villa":
                            curr_points = avl[-1]
                            new_points = curr_points + 0
                            avl.append(new_points)
                        case "Brighton":
                            curr_points = bha[-1]
                            new_points = curr_points + 0
                            bha.append(new_points)
                        case "Burnley":
                            curr_points = bur[-1]
                            new_points = curr_points + 0
                            bur.append(new_points)
                        case "Chelsea":
                            curr_points = che[-1]
                            new_points = curr_points + 0
                            che.append(new_points)
                        case "Crystal Palace":
                            curr_points = cry[-1]
                            new_points = curr_points + 0
                            cry.append(new_points)
                        case "Everton":
                            curr_points = eve[-1]
                            new_points = curr_points + 0
                            eve.append(new_points)
                        case "Fulham":
                            curr_points = ful[-1]
                            new_points = curr_points + 0
                            ful.append(new_points)
                        case "Leeds United":
                            curr_points = lee[-1]
                            new_points = curr_points + 0
                            lee.append(new_points)
                        case "Leicester City":
                            curr_points = lei[-1]
                            new_points = curr_points + 0
                            lei.append(new_points)
                        case "Liverpool":
                            curr_points = liv[-1]
                            new_points = curr_points + 0
                            liv.append(new_points)
                        case "Manchester City":
                            curr_points = mci[-1]
                            new_points = curr_points + 0
                            mci.append(new_points)
                        case "Manchester United":
                            curr_points = mun[-1]
                            new_points = curr_points + 0
                            mun.append(new_points)
                        case "Newcastle United":
                            curr_points = new[-1]
                            new_points = curr_points + 0
                            new.append(new_points)
                        case "Sheffield United":
                            curr_points = shu[-1]
                            new_points = curr_points + 0
                            shu.append(new_points)
                        case "Southampton":
                            curr_points = sou[-1]
                            new_points = curr_points + 0
                            sou.append(new_points)
                        case "Tottenham Hotspur":
                            curr_points = tot[-1]
                            new_points = curr_points + 0
                            tot.append(new_points)
                        case "West Bromwich Albion":
                            curr_points = wba[-1]
                            new_points = curr_points + 0
                            wba.append(new_points)
                        case "West Ham United":
                            curr_points = whu[-1]
                            new_points = curr_points + 0
                            whu.append(new_points)
                        case "Wolverhampton Wanderers":
                            curr_points = wol[-1]
                            new_points = curr_points + 0
                            wol.append(new_points)
                
                case 'A':
                    match ht:
                        case "Arsenal":
                            curr_points = ars[-1]
                            new_points = curr_points + 0
                            ars.append(new_points)
                        case "Aston Villa":
                            curr_points = avl[-1]
                            new_points = curr_points + 0
                            avl.append(new_points)
                        case "Brighton":
                            curr_points = bha[-1]
                            new_points = curr_points + 0
                            bha.append(new_points)
                        case "Burnley":
                            curr_points = bur[-1]
                            new_points = curr_points + 0
                            bur.append(new_points)
                        case "Chelsea":
                            curr_points = che[-1]
                            new_points = curr_points + 0
                            che.append(new_points)
                        case "Crystal Palace":
                            curr_points = cry[-1]
                            new_points = curr_points + 0
                            cry.append(new_points)
                        case "Everton":
                            curr_points = eve[-1]
                            new_points = curr_points + 0
                            eve.append(new_points)
                        case "Fulham":
                            curr_points = ful[-1]
                            new_points = curr_points + 0
                            ful.append(new_points)
                        case "Leeds United":
                            curr_points = lee[-1]
                            new_points = curr_points + 0
                            lee.append(new_points)
                        case "Leicester City":
                            curr_points = lei[-1]
                            new_points = curr_points + 0
                            lei.append(new_points)
                        case "Liverpool":
                            curr_points = liv[-1]
                            new_points = curr_points + 0
                            liv.append(new_points)
                        case "Manchester City":
                            curr_points = mci[-1]
                            new_points = curr_points + 0
                            mci.append(new_points)
                        case "Manchester United":
                            curr_points = mun[-1]
                            new_points = curr_points + 0
                            mun.append(new_points)
                        case "Newcastle United":
                            curr_points = new[-1]
                            new_points = curr_points + 0
                            new.append(new_points)
                        case "Sheffield United":
                            curr_points = shu[-1]
                            new_points = curr_points + 0
                            shu.append(new_points)
                        case "Southampton":
                            curr_points = sou[-1]
                            new_points = curr_points + 0
                            sou.append(new_points)
                        case "Tottenham Hotspur":
                            curr_points = tot[-1]
                            new_points = curr_points + 0
                            tot.append(new_points)
                        case "West Bromwich Albion":
                            curr_points = wba[-1]
                            new_points = curr_points + 0
                            wba.append(new_points)
                        case "West Ham United":
                            curr_points = whu[-1]
                            new_points = curr_points + 0
                            whu.append(new_points)
                        case "Wolverhampton Wanderers":
                            curr_points = wol[-1]
                            new_points = curr_points + 0
                            wol.append(new_points)
                                
                    match at:
                        case "Arsenal":
                            curr_points = ars[-1]
                            new_points = curr_points + 3
                            ars.append(new_points)
                        case "Aston Villa":
                            curr_points = avl[-1]
                            new_points = curr_points + 3
                            avl.append(new_points)
                        case "Brighton":
                            curr_points = bha[-1]
                            new_points = curr_points + 3
                            bha.append(new_points)
                        case "Burnley":
                            curr_points = bur[-1]
                            new_points = curr_points + 3
                            bur.append(new_points)
                        case "Chelsea":
                            curr_points = che[-1]
                            new_points = curr_points + 3
                            che.append(new_points)
                        case "Crystal Palace":
                            curr_points = cry[-1]
                            new_points = curr_points + 3
                            cry.append(new_points)
                        case "Everton":
                            curr_points = eve[-1]
                            new_points = curr_points + 3
                            eve.append(new_points)
                        case "Fulham":
                            curr_points = ful[-1]
                            new_points = curr_points + 3
                            ful.append(new_points)
                        case "Leeds United":
                            curr_points = lee[-1]
                            new_points = curr_points + 3
                            lee.append(new_points)
                        case "Leicester City":
                            curr_points = lei[-1]
                            new_points = curr_points + 3
                            lei.append(new_points)
                        case "Liverpool":
                            curr_points = liv[-1]
                            new_points = curr_points + 3
                            liv.append(new_points)
                        case "Manchester City":
                            curr_points = mci[-1]
                            new_points = curr_points + 3
                            mci.append(new_points)
                        case "Manchester United":
                            curr_points = mun[-1]
                            new_points = curr_points + 3
                            mun.append(new_points)
                        case "Newcastle United":
                            curr_points = new[-1]
                            new_points = curr_points + 3
                            new.append(new_points)
                        case "Sheffield United":
                            curr_points = shu[-1]
                            new_points = curr_points + 3
                            shu.append(new_points)
                        case "Southampton":
                            curr_points = sou[-1]
                            new_points = curr_points + 3
                            sou.append(new_points)
                        case "Tottenham Hotspur":
                            curr_points = tot[-1]
                            new_points = curr_points + 3
                            tot.append(new_points)
                        case "West Bromwich Albion":
                            curr_points = wba[-1]
                            new_points = curr_points + 3
                            wba.append(new_points)
                        case "West Ham United":
                            curr_points = whu[-1]
                            new_points = curr_points + 3
                            whu.append(new_points)
                        case "Wolverhampton Wanderers":
                            curr_points = wol[-1]
                            new_points = curr_points + 3
                            wol.append(new_points)
                
                case 'D':
                    match ht:
                        case "Arsenal":
                            curr_points = ars[-1]
                            new_points = curr_points + 1
                            ars.append(new_points)
                        case "Aston Villa":
                            curr_points = avl[-1]
                            new_points = curr_points + 1
                            avl.append(new_points)
                        case "Brighton":
                            curr_points = bha[-1]
                            new_points = curr_points + 1
                            bha.append(new_points)
                        case "Burnley":
                            curr_points = bur[-1]
                            new_points = curr_points + 1
                            bur.append(new_points)
                        case "Chelsea":
                            curr_points = che[-1]
                            new_points = curr_points + 1
                            che.append(new_points)
                        case "Crystal Palace":
                            curr_points = cry[-1]
                            new_points = curr_points + 1
                            cry.append(new_points)
                        case "Everton":
                            curr_points = eve[-1]
                            new_points = curr_points + 1
                            eve.append(new_points)
                        case "Fulham":
                            curr_points = ful[-1]
                            new_points = curr_points + 1
                            ful.append(new_points)
                        case "Leeds United":
                            curr_points = lee[-1]
                            new_points = curr_points + 1
                            lee.append(new_points)
                        case "Leicester City":
                            curr_points = lei[-1]
                            new_points = curr_points + 1
                            lei.append(new_points)
                        case "Liverpool":
                            curr_points = liv[-1]
                            new_points = curr_points + 1
                            liv.append(new_points)
                        case "Manchester City":
                            curr_points = mci[-1]
                            new_points = curr_points + 1
                            mci.append(new_points)
                        case "Manchester United":
                            curr_points = mun[-1]
                            new_points = curr_points + 1
                            mun.append(new_points)
                        case "Newcastle United":
                            curr_points = new[-1]
                            new_points = curr_points + 1
                            new.append(new_points)
                        case "Sheffield United":
                            curr_points = shu[-1]
                            new_points = curr_points + 1
                            shu.append(new_points)
                        case "Southampton":
                            curr_points = sou[-1]
                            new_points = curr_points + 1
                            sou.append(new_points)
                        case "Tottenham Hotspur":
                            curr_points = tot[-1]
                            new_points = curr_points + 1
                            tot.append(new_points)
                        case "West Bromwich Albion":
                            curr_points = wba[-1]
                            new_points = curr_points + 1
                            wba.append(new_points)
                        case "West Ham United":
                            curr_points = whu[-1]
                            new_points = curr_points + 1
                            whu.append(new_points)
                        case "Wolverhampton Wanderers":
                            curr_points = wol[-1]
                            new_points = curr_points + 1
                            wol.append(new_points)
                                
                    match at:
                        case "Arsenal":
                            curr_points = ars[-1]
                            new_points = curr_points + 1
                            ars.append(new_points)
                        case "Aston Villa":
                            curr_points = avl[-1]
                            new_points = curr_points + 1
                            avl.append(new_points)
                        case "Brighton":
                            curr_points = bha[-1]
                            new_points = curr_points + 1
                            bha.append(new_points)
                        case "Burnley":
                            curr_points = bur[-1]
                            new_points = curr_points + 1
                            bur.append(new_points)
                        case "Chelsea":
                            curr_points = che[-1]
                            new_points = curr_points + 1
                            che.append(new_points)
                        case "Crystal Palace":
                            curr_points = cry[-1]
                            new_points = curr_points + 1
                            cry.append(new_points)
                        case "Everton":
                            curr_points = eve[-1]
                            new_points = curr_points + 1
                            eve.append(new_points)
                        case "Fulham":
                            curr_points = ful[-1]
                            new_points = curr_points + 1
                            ful.append(new_points)
                        case "Leeds United":
                            curr_points = lee[-1]
                            new_points = curr_points + 1
                            lee.append(new_points)
                        case "Leicester City":
                            curr_points = lei[-1]
                            new_points = curr_points + 1
                            lei.append(new_points)
                        case "Liverpool":
                            curr_points = liv[-1]
                            new_points = curr_points + 1
                            liv.append(new_points)
                        case "Manchester City":
                            curr_points = mci[-1]
                            new_points = curr_points + 1
                            mci.append(new_points)
                        case "Manchester United":
                            curr_points = mun[-1]
                            new_points = curr_points + 1
                            mun.append(new_points)
                        case "Newcastle United":
                            curr_points = new[-1]
                            new_points = curr_points + 1
                            new.append(new_points)
                        case "Sheffield United":
                            curr_points = shu[-1]
                            new_points = curr_points + 1
                            shu.append(new_points)
                        case "Southampton":
                            curr_points = sou[-1]
                            new_points = curr_points + 1
                            sou.append(new_points)
                        case "Tottenham Hotspur":
                            curr_points = tot[-1]
                            new_points = curr_points + 1
                            tot.append(new_points)
                        case "West Bromwich Albion":
                            curr_points = wba[-1]
                            new_points = curr_points + 1
                            wba.append(new_points)
                        case "West Ham United":
                            curr_points = whu[-1]
                            new_points = curr_points + 1
                            whu.append(new_points)
                        case "Wolverhampton Wanderers":
                            curr_points = wol[-1]
                            new_points = curr_points + 1
                            wol.append(new_points)
        
        fig, ax = plt.subplots()
        
        fig.set_figwidth(20)
        fig.set_figheight(10)
        
        # now plot
        ax.plot(gw, ars, color="red", marker='o', markerfacecolor="whitesmoke", label="Arsenal")
        ax.plot(gw, avl, color="darkred", marker='o', markerfacecolor="steelblue", label="Aston Villa")
        ax.plot(gw, bha, color="whitesmoke", marker='o', markerfacecolor="dodgerblue", label="Brighton & Hove Albion")
        ax.plot(gw, bur, color="skyblue", marker='o', markerfacecolor="yellow", label="Burnley")
        ax.plot(gw, che, color="royalblue", marker='o', markerfacecolor="whitesmoke", label="Chelsea")
        ax.plot(gw, cry, color="red", marker='o', markerfacecolor="blue", label="Crystal Palace")
        ax.plot(gw, eve, color="mediumblue", marker='o', markerfacecolor="whitesmoke", label="Everton")
        ax.plot(gw, ful, color="whitesmoke", marker='o', markerfacecolor="black", label="Fulham")
        ax.plot(gw, lee, color="whitesmoke", marker='o', markerfacecolor="yellow", label="Leeds United")
        ax.plot(gw, lei, color="dodgerblue", marker='o', markerfacecolor="whitesmoke", label="Leicester City")
        ax.plot(gw, liv, color="red", marker='o', markerfacecolor="red", label="Liverpool")
        ax.plot(gw, mci, color="deepskyblue", marker='o', markerfacecolor="whitesmoke", label="Manchester City")
        ax.plot(gw, mun, color="red", marker='o', markerfacecolor="black", label="Manchester United")
        ax.plot(gw, new, color="black", marker='o', markerfacecolor="whitesmoke", label="Newcastle United")
        ax.plot(gw, shu, color="red", marker='o', markerfacecolor="yellow", label="Sheffield United")
        ax.plot(gw, sou, color="whitesmoke", marker='o', markerfacecolor="red", label="Southampton")
        ax.plot(gw, tot, color="whitesmoke", marker='o', markerfacecolor="whitesmoke", label="Tottenham Hotspur")
        ax.plot(gw, wba, color="whitesmoke", marker='o', markerfacecolor="navy", label="West Bromwich Albion")
        ax.plot(gw, whu, color="steelblue", marker='o', markerfacecolor="darkred", label="West Ham United")
        ax.plot(gw, wol, color="gold", marker='o', markerfacecolor="black", label="Wolverhampton Wanderers")
        
        ax.set_title("Season Summary")
        ax.set_facecolor("gainsboro")
        ax.set_xlabel("Gameweek")
        ax.set_ylabel("Points")
        ax.legend()
        
        plt.xticks(gw)

        plt.show()
        

def edit_database(conn, cursor):
    # enter with password, then edit database
    again = 'y'
    pw = input("Enter password: ")
    while pw != "prideoflondon":
        print("Access Denied.")
        again = input("Try again? (y/n): ")
        if again == 'y':
            pw = input("Enter password: ")
        
    # admin control
    print("Welcome, admin.")
    print("Choose a table to modify:\n  - fantasy\n  - players\n  - season\n  - exit")
    to_modify = input("  > ")
    
    while to_modify not in ["fantasy", "players", "season", "exit"]:
        print("\nInvalid table name. Choose again:")
        to_modify = input("  > ")
        
    if to_modify == "exit":
        return
    
    print("Choose an action:\n  - INSERT INTO\n  - DELETE FROM\n  - ALTER TABLE")
    action = input("  > ")
    while action not in ["INSERT INTO", "DELETE FROM", "ALTER TABLE"]:
        print("\nInvalid action. Choose again:")
        action = input("  > ")
        
    print("Build the WHERE condition:")
    if action == "INSERT INTO":
        print("Type the columns you would like to insert into:")
        cols = input(f"{action} {to_modify} ")
        print("Type the values you would like to insert into the specified columns:")
        vals = input(f"{action} {to_modify} {cols} VALUES ")
        
        query = f"{action} {to_modify} {cols} VALUES {vals};"
        
        cursor.execute(query)
        
        conn.commit()
        
        print("Database updated!")
    
    elif action == "DELETE FROM":
        print("Type the column you would like to filter by:")
        col = input(f"{action} {to_modify} WHERE ")
        print("Type the operator (=,<,>)")
        op = input(f"{action} {to_modify} WHERE {col}")
        print("Type the value:")
        val = input(f"{action} {to_modify} WHERE {col}{op}")
        
        query = f"{action} {to_modify} {col}{op}{val};"
        
        cursor.execute(query)
        
        conn.commit()
        
        print("Database updated!")
    
    else:
        print("Choose to ADD or DROP COLUMN")
        add_drop = input(f"{action} {to_modify} ")
        print("Enter the column name")
        col = input(f"{action} {to_modify} {add_drop} ")
        
        query = f"{action} {to_modify} {add_drop} {val};"
        
        cursor.execute(query)
        
        conn.commit()
        
        print("Database updated!")
        

if __name__ == "__main__":
    main()
    