This project explores how accurately the [Canadian Premier League (CPL)](https://www.cplsoccer.com/) can be predicted using data available from the CPL's API.
As it is designed to be a personal project that can be further developed as my skills in Python, mathematics, and statistics develop, it is setup in stages, with each stage intended to improve upon the last.


See Live Site @ https://jaspermclennan.github.io/cpl/

**STAGES**


**Stage 1: Past Season Success as Indicator of Current Team Strength**
For the first stage of this project, I decided to investigate how well a completed previous season can predict the strength of all teams in the current season. To begin this, I ingested all team data from the 2025 CPL season, and found the z score for each team's stat in each of the stat categories provided. I then used the .corrwith() function to determine which of the available stats most strongly correlated to having points in the table (and therefore to team success). Obviously, some stats need to be ignored (for example, total-wins would highly correlate to points, but doesnt really provide an insight)



**Stage 2: League History and Current Season Success as Indicator of Current Team Strength**
For this stage, I intend to undertake a similar process as above, but take into account all seasons of the CPL, with a decaying importance in how relevant a past season is to the current one.



**Stage 3: Introducing Player Performance and Impact**



**Stage 4: Combining Team and Player Performance**



**Stage 5: Considering Fixture Congestion, Player Fatigue, Travel Distance, Weather**



**Stage 5: Polling Socials to Track Matchday Squads and Update Projected XI**



**Stage 5: Determine Feasibility Integrating Machine Learning**





