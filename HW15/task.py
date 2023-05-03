import requests
import multiprocessing
import time

cities = [
    {"name": "Kyiv", "latitude": 50.45, "longitude": 30.51},
    {"name": "London", "latitude": 51.51, "longitude": -0.13},
    {"name": "New York", "latitude": 40.71, "longitude": -74.01},
    {"name": "Los Angeles", "latitude": 34.05, "longitude": -118.24},
    {"name": "Tokyo", "latitude": 35.69, "longitude": 139.69},
]

def get_temperature(city):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "hourly": "temperature_2m",
    }
    resp = requests.get(url=url, params=params)
    data = resp.json()
    temperature = data['hourly']['temperature_2m']
    print(f"{city['name']}: {temperature}°C")
    return temperature

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=5) as pool:
        temperatures = pool.map(get_temperature, cities)

    average_temperatures = {}
    for i in range(len(cities)):
        if temperatures[i] is not None:
            average_temperatures[cities[i]['name']] = sum(temperatures[i])/len(temperatures[i])

    hottest_city = max(average_temperatures, key=average_temperatures.get)
    print(f"\n{hottest_city} is the hottest city with an average temperature of {average_temperatures[hottest_city]:.1f}°C")

    print(f"Multiprocessing took {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    for city in cities:
        get_temperature(city)

    print(f"Program ended in {time.time() - start_time:.2f} seconds")
