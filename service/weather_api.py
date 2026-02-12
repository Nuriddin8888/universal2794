import requests

API_KEY = ""

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "uz"
    }

    try:
        a = requests.get(url, params=params)
        data = a.json()

        if a.status_code != 200:
            return None

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather

    except Exception as e:
        return None
