import requests
import pandas as pd
import numpy as np
import os


base_url = "https://api-sdp.cplsoccer.com/v1/cpl/football/seasons/cpl::Football_Season::c479ab0916a24c3390f1ce2c021ace54/stats/teams?locale=en-US"

# season_ids = {
#
#     "2021" : "2f07c39671b84933ad7bb1e1958a7427",
#     "2022" : "046f0ab31ba641c7b7bf27eb0dda4b9d",
#     "2023" : "fc0855108c9044218a84fc5d2bee0000",
#     "2024" : "6fb9e6fae4f24ce9bf4fa3172616a762",
#     "2025" : "fd43e1d61dfe4396a7356bc432de0007",
#     "2026" : "c479ab0916a24c3390f1ce2c021ace54",
# }

response = requests.get(base_url)

#check to make sure the request was successful
if response.status_code == 200:
    print("Request was successful")
else:
    print(f"Failed to retrieve data: {response.status_code}")


data = response.json()

rows = []
for team in data["teams"]:
    row = {
       
        "acronymName": team["acronymName"],
         "shortName": team["shortName"],
    }
    for stat in team["stats"]:
        row[stat["statsId"]] = stat["statsValue"]
    rows.append(row)

teams_data = pd.DataFrame(rows)


average_df =  teams_data.mean(numeric_only=True, axis=0)
stddev_df =  teams_data.std(numeric_only=True, axis=0)
zscore_df = (teams_data - average_df) / stddev_df

correlation_df = teams_data.corrwith(teams_data['total-points'],numeric_only=True)
strong_correlation_df = correlation_df[correlation_df.abs() > 0.7]


print(teams_data)

print("__________________________________________________________________________________________________________")

print(strong_correlation_df)


# os.makedirs("data/team", exist_ok=True)
# teams_data.to_csv("data/team/2026_team_data.csv", index=False, sep=';')