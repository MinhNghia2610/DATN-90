import requests

API_KEY = "4e536a8d913acd30bc2fa016dd57a1bb"
CITY = "Ho Chi Minh City"

def get_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric&lang=vi"
    )

    res = requests.get(url).json()

    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]

    return f"🌤️ Thời tiết {CITY}: {desc}, {temp}°C"
