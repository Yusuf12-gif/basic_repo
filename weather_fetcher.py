import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found or invalid API key!")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(city, api_key)
