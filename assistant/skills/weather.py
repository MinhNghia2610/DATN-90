import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"
CITY = "Hanoi"

def get_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric&lang=vi"
    )

    res = requests.get(url).json()

    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]

    return f"🌤️ Thời tiết {CITY}: {desc}, {temp}°C"
