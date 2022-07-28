#http://openweathermap.org/
#Key- 4cb1057e0ebe754b303b3ddc2c3c6bc5

#import stuff
import time
import json, requests
global zipcode
from urllib.request import urlopen

#welcome message
print("Welcome to the Weather Checker Program!")

time.sleep(1)

print("In this program, you can enter a US zip code to find out what the weather in that location!")


while True:
  try:
    zipcode = int(input("Enter the zip code: "))
  except ValueError:
    print ("Error! Only numbers are allowed.")
  if zipcode < 1:
    print ("Error! Only valid 5 digit zip codes are allowed.")
  elif zipcode > 99999:
    print ("Error! Only valid 5 digit zip codes are allowed.")
  else:
    break    

#get weather details by zip
base_url = "https://api.openweathermap.org/data/2.5/weather?"
apikey = "4cb1057e0ebe754b303b3ddc2c3c6bc5"
countrycode = "us"
units = "imperial"
url = f"{base_url}zip={zipcode},{countrycode}&appid={apikey}&units={units}"

with urlopen("https://api.openweathermap.org/data/2.5/weather?zip=63640,us&appid=4cb1057e0ebe754b303b3ddc2c3c6bc5&units=imperial") as response:
    source = response.read()

zipdata = json.loads(source)

for item in zipdata['main']:
  tempmin = item['main']["temp_min"]
  tempmax = item['main']["temp_max"]
  print(tempmin)
  #breaks here

#working until here....WARNING
base_url = "http://api.openweathermap.org/data/2.5/weather"
appid = "4cb1057e0ebe754b303b3ddc2c3c6bc5"
city = converted_city
url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print ()


response = requests.get(url)
unformated_data = response.json()

temp = unformated_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformated_data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")