import os
import dotenv
import requests

dotenv.load_dotenv(override=True)
API_KEY = os.environ.get('weather_api_key')
DAILY_PRED_COUNT = 8

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    
    filtered_data = data['list']
    filtered_data = filtered_data[:forecast_days * DAILY_PRED_COUNT]
    
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="tokyo", forecast_days=2, kind="Temperature"))