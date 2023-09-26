#utilizes GEOPY/OPENWEATHER API to determine the weather of a location based upon user input.
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
#pprint(location)
api_key = '3cf792a4f3be0e9964f39866b1e620a5'

app = Nominatim(user_agent="tutorial")
custom_theme = Theme({
            "night": "bold cornflower_blue", 
            "day": "bold yellow1"
        })

user_location = input("enter any location with proper capitilization to receive a weather report (or type 'q' to quit): ")

climate_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")
            
if climate_data.json()['cod'] == '404':
        print("unidentified location")
else:
                climate = climate_data.json()['weather'][0]['description']
                temperature = round(climate_data.json()['main']['feels_like'])
                longitude = float((climate_data.json()['coord']['lon']))
                latitude = float((climate_data.json()['coord']['lat']))

                now = datetime.now()
                UTC_minute = now.strftime(":%M")
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
                    if -140 <= longitude < -102 and 60<= latitude <= 150:
                                local_time = UTC_hour - 7
                                if local_time <0:
                                    local_time +=24
                    if -102 <= longitude < -84:
                                local_time = UTC_hour - 6
                                if local_time <0:
                                    local_time +=24     
                    if -84 <= longitude < -68:
                                local_time = UTC_hour - 5
                                if local_time <0:
                                    local_time +=24
                    if -68 <= longitude < -53:
                                local_time = UTC_hour - 4
                                if local_time <0:
                                    local_time +=24
                    if -53 <= longitude < -38:
                                local_time = UTC_hour - 3
                                if local_time <0:
                                    local_time +=24
                    if -22 <= longitude < 2 and 50<= latitude <= 165:
                                local_time = UTC_hour 
                                if local_time <0:
                                    local_time +=24
                    if -15 <= longitude < 4 and 0<= latitude <= 30:
                                local_time = UTC_hour
                                if local_time <0:
                                    local_time +=24
                    if 4 <= longitude < 22 and 0<= latitude <= 30:
                                local_time = UTC_hour + 1
                                if local_time <0:
                                    local_time +=24
                    if 22 <= longitude < 30:
                                local_time = UTC_hour + 2
                                if local_time <0:
                                    local_time +=24
                    if 30 <= longitude < 45: 
                                local_time = UTC_hour + 3
                                if local_time <0:
                                    local_time +=24
                    if 45 <= longitude < 52:
                                local_time = UTC_hour + 4
                                if local_time <0:
                                    local_time +=24
                    if 52 <= longitude < 75 and 30<= latitude <=75 :
                                local_time = UTC_hour + 5
                                if local_time <0:
                                    local_time +=24
                    if 75 <= longitude < 90 and 0<= latitude <=30 :
                                local_time = UTC_hour + 5.5
                                if local_time <0:
                                    local_time +=24
                    if 97 <= longitude < 116 and -5<= latitude <=20 :
                                local_time = UTC_hour + 7
                                if local_time <0:
                                    local_time +=24
                    if 75 <= longitude < 112 and 40<= latitude <=90 :
                                local_time = UTC_hour + 7
                                if local_time <0:
                                    local_time +=24
                    if 80 <= longitude < 135 and 20<= latitude <=55 :
                                local_time = UTC_hour + 8
                                if local_time <0:
                                    local_time +=24
                    if 112 <= longitude < 127 and -45<= latitude <=55 :
                                local_time = UTC_hour + 8
                                if local_time <0:
                                    local_time +=24
                    if 108 <= longitude < 132 and 50<= latitude <=75 :
                                local_time = UTC_hour + 9
                                if local_time <0:
                                    local_time +=24
                    if 124 <= longitude < 142 and -5<= latitude <=42 :
                                local_time = UTC_hour + 9
                                if local_time <0:
                                    local_time +=24
                    if 127 <= longitude < 142 and -45<= latitude <=-15 :
                                local_time = UTC_hour + 9.5
                                if local_time <0:
                                    local_time +=24
                    if 132 <= longitude < 142 and 45<= latitude <=70 :
                                local_time = UTC_hour + 10
                                if local_time <0:
                                    local_time +=24
                    if 142 <= longitude < 157 and -60<= latitude <=20 :
                                local_time = UTC_hour + 10
                                if local_time <0:
                                    local_time +=24
                                    
                    if 142 <= longitude < 157 and 55<= latitude <=70 :
                                local_time = UTC_hour + 11
                                if local_time <0:
                                    local_time +=24
                    if 157 <= longitude < 187 :
                                local_time = UTC_hour + 12
                                if local_time <0:
                                    local_time +=24
                    return (local_time)        
        
print(UTC_hour)

region_time_value = region_time(longitude)
print(region_time_value)

if 6 <= region_time_value <= 18:
                    console = Console(theme=custom_theme)
                    console.print(f"[day]WEATHER REPORT AT {region_time_value} {UTC_minute}[/day]")
                    console.print(f"[day]the elements in {user_location} are blending together to form {climate} and a temperature of {temperature} degrees °F[/day]")
elif region_time_value == 0:
                    print("error")
else:
                    console = Console(theme=custom_theme)
                    console.print(f"[night]WEATHER REPORT AT {region_time_value} {UTC_minute}[/night]")
                    console.print(f"[night]the elements in {user_location} are blending together to form {climate} and a temperature of {temperature} degrees °F[/night]")
 