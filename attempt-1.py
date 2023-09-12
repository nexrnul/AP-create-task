import requests

api_key = '3cf792a4f3be0e9964f39866b1e620a5'

user_location = input("enter location: ")

climate_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")

print(climate_data.json())

climate = climate_data.json()['weather'][0]['description']
temperature = climate_data.json()['main']['feels_like']

print("")
print("it feels like", temperature, "over in", user_location)
print("the elements in", user_location, "are blending together to form", climate)