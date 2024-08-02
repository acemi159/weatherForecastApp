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
def get_data(days):
    
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [30, 31, 33]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)
figure = px.line(x=d, y=t, labels={'x':'Date', 'y':'Temperature (C)'})

st.plotly_chart(figure)