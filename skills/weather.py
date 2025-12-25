import requests

API_KEY = "6bb4442b7cac8204b4aab0d5b1bbc6c8"

def get_weather(city="Hà Nội"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=vi"
    r = requests.get(url).json()
    return f"Thời tiết {city}: {r['weather'][0]['description']}, {r['main']['temp']} độ C"
