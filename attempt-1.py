#utilizes GEOPY API to determine the weather of a location based upon user input.
#This program also determines the local time of whatever city you input based on the UTC time and longitutde provided by the API.

import requests

from datetime import datetime

from geopy.geocoders import Nominatim
import time
from pprint import pprint
from rich.console import Console
from rich.theme import Theme
#UTC_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print(climate_data.json())
api_key = '3cf792a4f3be0e9964f39866b1e620a5'

user_location = input("enter any location with proper capitilization: ")

app = Nominatim(user_agent="tutorial")

location = app.geocode(user_location).raw

#pprint(location)

climate_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")

if climate_data.json()['cod'] == '404':
    print("unidentified location")
else:
    climate = climate_data.json()['weather'][0]['description']
    temperature = round(climate_data.json()['main']['feels_like'])
    longitude = float((climate_data.json()['coord']['lon']))
    latitude = float((climate_data.json()['coord']['lat']))

now = datetime.now()

UTC_minute = now.strftime(":%M%p")
UTC_hour = now.strftime("%H")
def region_time(longitude):
    UTC_hour = int(now.strftime("%H"))
    if -172.5 <= longitude < -157.5 and -50<= latitude <=0:
                local_time = UTC_hour - 11
                if local_time <0:
                    local_time +=24
    if -157.5 <= longitude < -135 and -30<= latitude <=0:
                local_time = UTC_hour - 10
                if local_time <0:
                    local_time +=24
    if -160 <= longitude < -141 and 50<= latitude <= 71:
                local_time = UTC_hour - 9
                if local_time <0:
                    local_time +=24
    if -135 <= longitude < -112 and 28<= latitude <= 60:
                local_time = UTC_hour - 8
                if local_time <0:
                    local_time +=24
    if -142 <= longitude < -92 and 60<= latitude <= 150:
                local_time = UTC_hour - 7
                if local_time <0:
                    local_time +=24
    if -114 <= longitude < -102 and 20<= latitude <= 60:
                local_time = UTC_hour - 7
                if local_time <0:
                    local_time +=24     

    if -97.5 <= longitude < -82.5:
                local_time = UTC_hour - 6
                if local_time <0:
                    local_time +=24
    if -82.5 <= longitude < -67.5:
                local_time = UTC_hour - 4
                if local_time <0:
                    local_time +=24
    if -67.5 <= longitude < -52.5:
                local_time = UTC_hour - 3
                if local_time <0:
                    local_time +=24
    if -52.5 <= longitude < -37.5:
                local_time = UTC_hour - 2
                if local_time <0:
                    local_time +=24
    if -37.5 <= longitude < -22.5:
                local_time = UTC_hour - 1
                if local_time <0:
                    local_time +=24
    if -22.5 <= longitude < -7.5:
                local_time = UTC_hour 
                if local_time <0:
                    local_time +=24
    if -7.5 <= longitude < 7.5:
                local_time = UTC_hour + 1
                if local_time <0:
                    local_time +=24
    if 7.5 <= longitude < 22.5:
                local_time = UTC_hour + 2
                if local_time <0:
                    local_time +=24
    if 22.5 <= longitude < 37.5:
                local_time = UTC_hour + 3
                if local_time <0:
                    local_time +=24
    if 37.5 <= longitude < 52.5:
                local_time = UTC_hour + 4
                if local_time <0:
                    local_time +=24
    if 52.5 <= longitude < 67.5:
                local_time = UTC_hour + 5
                if local_time <0:
                    ocal_time +=24
    if 67.5 <= longitude < 82.5:
                local_time = UTC_hour + 6
                if local_time <0:
                    local_time +=24
    if 82.5 <= longitude < 97.5:
                local_time = UTC_hour + 7
                if local_time <0:
                    local_time +=24
    if 97.5 <= longitude < 112.5:
                local_time = UTC_hour + 8
                if local_time <0:
                   local_time +=24
    if 112.5 <= longitude < 127.5:
                local_time = UTC_hour + 9
                if local_time <0:
                    local_time +=24
    if 127.5 <= longitude < 142.5:
                local_time = UTC_hour + 10
                if local_time <0:
                    local_time +=24
    if 142.5 <= longitude < 157.5:
                local_time = UTC_hour + 11
                if local_time <0:
                    local_time +=24
    if 157.5 <= longitude < 172.5:
                local_time = UTC_hour + 12
                if local_time <0:
                    local_time +=24
    if 172.5 <= longitude < 180:
                local_time = UTC_hour + 13
                if local_time <0:
                    local_time +=24
    return (local_time)

print(UTC_hour)

custom_theme = Theme({
    "night": "bold cornflower_blue", 
    "day": "bold yellow1"
    })

region_time_value = region_time(longitude)
print(region_time_value)


if 6 <= region_time_value <= 18:
    console = Console(theme=custom_theme)
    console.print("WEATHER REPORT AT", (region_time_value),(UTC_minute), style="day")
    console.print("the elements in", user_location, "are blending together to form", climate, "and a temperature of", temperature, "degrees °F", style="day")
elif region_time_value == 0:
    print("error")
else:
    console = Console(theme=custom_theme)
    console.print("WEATHER REPORT AT", region_time_value,(UTC_minute), style="night")
    console.print("the elements in", user_location, "are blending together to form", climate, "and a temperature of", temperature, "degrees °F", style="night")

