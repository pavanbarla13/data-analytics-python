# Weather Data Analysis (Beginner)
import requests

city = input("Enter city name: ")
api_key = "your_api_key_here"  # use free API or leave dummy
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

if data["cod"] != "404":
    main = data["main"]
    print(f"Temperature: {main['temp']} K")
    print(f"Humidity: {main['humidity']}%")
else:
    print("City not found")