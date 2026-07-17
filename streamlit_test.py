import streamlit as st
from source.single_season_analyzer import fetch_team_data


st.title("Jasper's CPL Prediction Engine")

st.text("League Data for the 2025 CPL Season")
teams_data = fetch_team_data()
st.dataframe(teams_data, column_config={"acronymName": st.column_config.Column(pinned=True)})

