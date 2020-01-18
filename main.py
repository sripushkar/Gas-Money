import requests
import json
import xml.etree.ElementTree as ET


url = "https://www.fueleconomy.gov/ws/rest/fuelprices"
prices = requests.get(url)

pricesRoot = ET.fromstring(prices.content)

dieselPrice = pricesRoot[1].text
regularPrice = pricesRoot[7].text
midgradePrice = pricesRoot[5].text
premiumPrice = pricesRoot[6].text



#Gets the most recent national average price on gas
#price = jsonGasPrices["series"][0]["data"][0][1]


#print("Welcome to Gas Money Calculator by Sri Julapally")
#print("Make sure to only enter numbers for the below questions, or the program will fail.")

#The variables needed to calculate gas price
fuelTypeInput = int(input("What type of fuel does your vehicle use?\nDiesel[0]\nRegular[1]\nMidgrade[2]\nPremium[3]\nPlease input the corresponding number. "))
fuelEcon = float(input("What is the fuel economy of your car in miles per gallon? "))
people = int(input("How many people are you driving? "))
distance = float(input("How many miles are you driving? You can use decimals. "))

#Calculates the price per person
if fuelTypeInput == 0:
    price = dieselPrice
elif fuelTypeInput == 2:
    price = midgradePrice
elif fuelTypeInput == 3:
    price = premiumPrice
else:
    price = regularPrice

price = float(price)
gasMoney = (distance*price)/(fuelEcon*people)

print("Each person will owe you $" + str(round(gasMoney, 2)))
