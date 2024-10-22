import requests

city = input("What city's weather are you looking for today? ")

url = "https://api.weatherapi.com/v1/current.json?key=ba7ca2ac04eb4594867191825242010&q="+city+"&aqi=no"

response = requests.get(url)
weather_response = response.json()

temp = weather_response.get('current').get('temp_f')
description = weather_response.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, 'and', temp)