import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "5f5a5400208d83733b0f3e01ca8b5056"

def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    print(url)
    weather_data = response.json()

    if weather_data["cod"] == "404":
        print("City not found.")
    else:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

def main():
    city = input("Enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
