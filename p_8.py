team1_runs = int(input("Enter total runs scored by Team 1: "))
team1_overs = float(input("Enter total overs faced by Team 1: "))
team1_wickets = int(input("Enter total wickets lost by Team 1: "))
team2_runs = int(input("Enter total runs scored by Team 2: "))
team2_overs = float(input("Enter total overs faced by Team 2: "))
team2_wickets = int(input("Enter total wickets lost by Team 2: "))

# calculate net run rate for both teams
team1_nrr = round((team1_runs / team1_overs) - (team2_runs / team2_overs), 2)
team2_nrr = round((team2_runs / team2_overs) - (team1_runs / team1_overs), 2)

# determine which team tops the points table based on NRR
if team1_nrr > team2_nrr:
    print("Team 1 has a higher net run rate.")
elif team2_nrr > team1_nrr:
    print("Team 2 has a higher net run rate.")
else:
    # in case of a tie, use wickets lost as the tie-breaker
    if team1_wickets < team2_wickets:
        print("Team 1 tops the points table based on net run rate and wickets lost.")
    elif team2_wickets < team1_wickets:
        print("Team 2 tops the points table based on net run rate and wickets lost.")
    else:
        print("The teams are tied on net run rate and wickets lost.")