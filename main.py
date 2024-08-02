import streamlit as st
import pandas as pd


st.title("Weather Forecast for the Next Days")

st.text("Place")

place = st.text_input("Place: ")

days = st.slider("Forecast days: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to review", 
                      ("Temperature", "Sky"))

if place and days and option:
    st.subheader(f"{option} for the next {days} in {place}")

