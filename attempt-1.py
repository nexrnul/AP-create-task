import requests

from datetime import datetime

now = datetime.now()

local_time = now.strftime("%m/%d/%Y, %H:%M:%S")

print(local_time)

def identify_region():

    return

api_key = '3cf792a4f3be0e9964f39866b1e620a5'

user_location = input("enter location: ")

from geopy.geocoders import Nominatim
import time
from pprint import pprint

app = Nominatim(user_agent="tutorial")

location = app.geocode(user_location).raw

pprint(location)

climate_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")

if climate_data.json()['cod'] == '404':
    print("unidentified location")
else:
    climate = climate_data.json()['weather'][0]['description']
temperature = round(climate_data.json()['main']['feels_like'])
longitude = climate_date.json()['coord']['lon']


print(climate_data.json())


from rich import print
print("[bold cornflower_blue]WEATHER[/] [bold cornflower_blue]REPORT[/]")
print("the elements in", user_location, "are blending together to form", climate, "and a temperature of", temperature, "degrees °F")

