import requests
import pandas as pd
import numpy as np
import os


# Set base url to fetch TEAM data from the API

base_url = "https://api-sdp.cplsoccer.com/v1/cpl/football/seasons/cpl::Football_Season::c479ab0916a24c3390f1ce2c021ace54/stats/teams?locale=en-US"


#make all season ids into a dictionary we can loop through
season_ids = {

    "2021" : "2f07c39671b84933ad7bb1e1958a7427",
    "2022" : "046f0ab31ba641c7b7bf27eb0dda4b9d",
    "2023" : "fc0855108c9044218a84fc5d2bee0000",
    "2024" : "6fb9e6fae4f24ce9bf4fa3172616a762",
    "2025" : "fd43e1d61dfe4396a7356bc432de0007",
    "2026" : "c479ab0916a24c3390f1ce2c021ace54",
}

#for each season in cpl history we want to make a request to the api to fetch all the possible team stats
for season in season_ids:
    season_id = season_ids[season]
    base_url = f"https://api-sdp.cplsoccer.com/v1/cpl/football/seasons/cpl::Football_Season::{season_id}/stats/teams?locale=en-US"

    response = requests.get(base_url)

    #check to make sure the request was successful abd if it is print what season is being rocessed
    if response.status_code == 200:
        print("Request was successful for year:", season)
    else:
        print(f"Failed to retrieve data for year {season}: {response.status_code}")


    data = response.json()

    rows = []
    for team in data["teams"]:
        row = {
        
            "acronymName": team["acronymName"],
            # "shortName": team["shortName"],
        }
        for stat in team["stats"]:
            row[stat["statsId"]] = stat["statsValue"]
        rows.append(row)

    teams_data = pd.DataFrame(rows)  # Select only numeric columns



#make a df with the average of each team stat coumn
    average_df =  teams_data.mean(numeric_only=True, axis=0)
#make a df with the stddev of each team stat column
    stddev_df =  teams_data.std(numeric_only=True, axis=0)
#use the average and stddev df to calculate the zscore for each team stat column
#we do this so that we can easily compare the importance of each stat to total points, regardless of how a stat is represented
    zscore_df = (teams_data - average_df) / stddev_df


#using the .corr library funciotn we can obtain the correlation of each stat to total points, thus giving a bit of a guide as to how 
# relevant each stat may be to a team "winning"

    correlation_df = teams_data.corrwith(teams_data['total-points'],numeric_only=True)

    #we can filter the correltaion to only strogly correlated stats so as to remove noise from data
    strong_correlation_df = correlation_df[correlation_df.abs() > 0.7]


  #  print(teams_data)

    print("__________________________________________________________________________________________________________")


    print(zscore_df)


    os.makedirs("data/team", exist_ok=True)
    teams_data.to_csv(f"data/team/{season}_team_data.csv", index=False, sep=';')