import requests
import pandas as pd
import numpy as np
import os


# Set base url to fetch TEAM data from the API

base_url = "https://api-sdp.cplsoccer.com/v1/cpl/football/seasons/cpl::Football_Season::c479ab0916a24c3390f1ce2c021ace54/stats/teams?locale=en-US"


#make all season ids into a dictionary we can loop through
# season_ids = {

#     "2021" : "2f07c39671b84933ad7bb1e1958a7427",
#     "2022" : "046f0ab31ba641c7b7bf27eb0dda4b9d",
#     "2023" : "fc0855108c9044218a84fc5d2bee0000",
#     "2024" : "6fb9e6fae4f24ce9bf4fa3172616a762",
#     "2025" : "fd43e1d61dfe4396a7356bc432de0007",
#     "2026" : "c479ab0916a24c3390f1ce2c021ace54",
# }



response = requests.get(base_url)

#check to make sure the request was successful abd if it is print what season is being rocessed
if response.status_code == 200:
    print("Request was successful")
else:
    print(f"Failed to retrieve data: {response.status_code}")


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

teams_data = pd.DataFrame(rows)

print(teams_data)



#make a df with the average of each team stat coumn
print("______________________________________________LEAGUE STAT AVERAGES____________________________________________________________")
average_df =  teams_data.mean(numeric_only=True, axis=0)
print(average_df)


#make a df with the stddev of each team stat column
print("______________________________________________LEAGUE STAT STANDARD DEVIATIONS____________________________________________________________")
stddev_df =  teams_data.std(numeric_only=True, axis=0)
print(stddev_df)


#use the average and stddev df to calculate the zscore for each team stat column
#we do this so that we can easily compare the importance of each stat to total points, regardless of how a stat is represented
print("______________________________________________LEAGUE STAT Z-SCORES FOR EACH TEAM____________________________________________________________")
zscore_df = (teams_data - average_df) / stddev_df
zscore_df = zscore_df.assign(acronymName=teams_data['acronymName'])  # Insert the acronymName column back into the zscore_df
zscore_df = zscore_df[['acronymName'] + [col for col in zscore_df.columns if col != 'acronymName']]  # Reorder columns
print(zscore_df)


# # #using the .corr library funciotn we can obtain the correlation of each stat to total points, thus giving a bit of a guide as to how 
# # # relevant each stat may be to a team "winning"

# # correlation_df = teams_data.corrwith(teams_data['total-points'],numeric_only=True)

# # #we can filter the correltaion to only strogly correlated stats so as to remove noise from data
# # strong_correlation_df = correlation_df[correlation_df.abs() > 0.7]


# #  print(teams_data)

# print("__________________________________________________________________________________________________________")


# print(teams_data)


# os.makedirs("data/team/single_season", exist_ok=True)
# teams_data.to_csv(f"data/team/single_season/single_season_2026_team_data.csv", index=False, sep=';')