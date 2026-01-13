import requests

API_KEY = "4a10b673283554a0919213e6c8b5df53"

city = input("City: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
    print("Temperature:", data["main"]["temp"], "°C")
except KeyError:
    print("City not found")


