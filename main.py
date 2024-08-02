from backend import get_data

import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

st.text("Place")

place = st.text_input("Place: ")

days = st.slider("Forecast days: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to review", 
                      ("Temperature", "Sky"))

if place and days and option:
    st.subheader(f"{option} for the next {days} in {place}")

# Create the plot
d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={'x':'Date', 'y':'Temperature (C)'})

st.plotly_chart(figure)