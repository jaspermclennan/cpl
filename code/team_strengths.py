import cpl.code.multi_season_fetcher as multi_season_fetcher

print(multi_season_fetcher.strong_correlation_df)



team_ids = {

    "0" : "EDM",
    "1" : "ITO",
    "2" : "VAL",
    "3" : "HFX",
    "4" : "CAV",
    "5" : "PAC",
    "6" : "ATO",
    "7" : " FOR", 
    
    }





# strength_for_stat = zscore_for_stat * correlation_for_stat

# team_rating = all strengths for stat added together

# figure out a way to weight stats from older years as less important. 