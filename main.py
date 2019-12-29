import requests
import json

#Enter your API Key from https://www.eia.gov/opendata/qb.php?category=711295
API_KEY = ""
url = "http://api.eia.gov/series/?api_key="+API_KEY+"&series_id=TOTAL.MGUCUUS.M"

#Gets the most recent national average price on gas
gasPrices = requests.get(url)
jsonGasPrices = gasPrices.json()
price = jsonGasPrices["series"][0]["data"][0][1]


print("Welcome to Gas Money Calculator by Sri Julapally")
print("Make sure to only enter numbers for the below questions, or the program will fail.")

#The variables needed to calculate gas price
fuelEcon = float(input("What is the fuel economy of your car in miles per gallon? "))
people = int(input("How many people are you driving? "))
distance = float(input("How many miles are you driving? You can use decimals. "))

#Calculates the price per person
gasMoney = (distance*price)/(fuelEcon*people)

print("Each person will owe you $" + str(round(gasMoney, 2)))
