import requests
import json
import xml.etree.ElementTree as ET

print("Welcome to Gas Money Calculator by Sri Julapally")
print("Make sure to only enter appropriate inputs for the below questions, or the program will fail.")

pricesUrl = "https://www.fueleconomy.gov/ws/rest/fuelprices"
pricesList = requests.get(pricesUrl)
pricesRoot = ET.fromstring(pricesList.content)

dieselPrice = pricesRoot[1].text
regularPrice = pricesRoot[7].text
midgradePrice = pricesRoot[5].text
premiumPrice = pricesRoot[6].text

make = input("What is the make(brand) of your car? ")
year = input("What is the year of your car? ")
carUrl = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year="+year+"&make="+make
carList = requests.get(carUrl)
carsRoot = ET.fromstring(carList.content)

print("These are the models with avaliable data:")

for models in carsRoot.findall("menuItem"):
    model = models.find("value").text
    print(model+"\n")

modelSelection = input("Do you see your model in this list? If you do, please type in the model name now. If you do not see it, please enter 0, and you will be prompted to manually enter the fuel economy.")


#The variables needed to calculate gas price
fuelTypeInput = int(input("What type of fuel does your vehicle use?\nDiesel[0]\nRegular[1]\nMidgrade[2]\nPremium[3]\nPlease input the corresponding number. "))
fuelEcon = float(input("What is the fuel economy of your car in miles per gallon? "))
people = int(input("How many people are you driving? "))
distance = float(input("How many miles are you driving? You can use decimals. "))

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
