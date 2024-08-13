from django.shortcuts import render
import requests
import datetime
from decouple import config

def index(request):
    API_KEY = config('API_KEY')
    # Weatherbit API endpoints
    current_weather_url = "https://api.weatherbit.io/v2.0/current?city={}&key={}"
    forecast_url = "https://api.weatherbit.io/v2.0/forecast/daily?city={}&key={}&days=5"

    if request.method == "POST":
        city1 = request.POST.get('city1')
        city2 = request.POST.get("city2", None)

        weather_data1, daily_forecast1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecast2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_url)
        else:
            weather_data2, daily_forecast2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecast1": daily_forecast1,
            "weather_data2": weather_data2,
            "daily_forecast2": daily_forecast2,
        }
        return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html")
    
def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    if response.get("error"):
        print(f"Error fetching weather data for {city}: {response['error']['message']}")
        return None, None

    weather_data = {
        "city": response['data'][0]['city_name'],
        "temperature": response['data'][0]['temp'],
        "description": response['data'][0]['weather']['description'],
        "icon": response['data'][0]['weather']['icon']
    }

    forecast_response = requests.get(forecast_url.format(city, api_key)).json()

    daily_forecast = []
    for daily_data in forecast_response['data']:
        daily_forecast.append(
            {
                "day": datetime.datetime.strptime(daily_data['valid_date'], "%Y-%m-%d").strftime("%A"),
                "min_temp": daily_data['min_temp'],
                "max_temp": daily_data['max_temp'],
                "description": daily_data['weather']['description'],
                "icon": f"https://www.weatherbit.io/static/img/icons/{daily_data['weather']['icon']}.png"
            }
        )
    return weather_data, daily_forecast