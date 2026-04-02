import requests

def get_current_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": 18.52,
        "longitude": 73.85,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    # Basic validation (don't trust API blindly)
    if response.status_code != 200:
        raise Exception("Failed to fetch weather data")

    data = response.json()

    return {
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"]
    }