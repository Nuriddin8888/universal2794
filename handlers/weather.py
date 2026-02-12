import aiohttp

API_KEY = ""

async def get_weather_async(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    b = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "uz"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=b) as response:
            if response.status != 200:
                return None
            
            data = await response.json()

            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
