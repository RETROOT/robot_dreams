import requests

def get_weather(city):
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"

    # Отримання координат міста за допомогою API геокодування
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get(geocoding_url, params=params)
    data = response.json()

    if "results" in data:
        result = data["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]

        # Отримання погодних даних за допомогою API погоди
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
        }
        response = requests.get(weather_url, params=params)
        data = response.json()

        if "hourly" in data:
            temperature = data["hourly"]["temperature_2m"]
            print(f"Погода в місті {city}: {temperature}°C")
        else:
            print("Не вдалося отримати погодні дані.")
    else:
        print("Не вдалося знайти координати для введеного міста.")

# Отримання назви міста від користувача
city = input("Введіть назву міста: ")
get_weather(city)
