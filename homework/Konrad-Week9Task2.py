#Name:Zac Konrad

import json, requests


print ("Welcome to Find My Weather")

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "69b9df46be1cb29d6530ff604a10888e"

try:
  city_zip = input("Enter the name of your city or zip code here:")

except:
      print("Check spelling or Zip code and try again")
      print()
###Getting error and need to prompt to try again  

print (city_zip)

url = f"{base_url}?q={city_zip}&units=imperial&APPID={appid}"
print(url)
print ()

response = requests.get(url)
unformated_data = response.json()  

#print (unformated_data)

###need to show the city or zip code at the beginin of unformated_data
###name = unformated_data["main"]["name"]
###print(f"The weather area you searched for was: {name}")

temp = unformated_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformated_data["main"]["temp"]
print(f"The max temp is: {temp_max}")
    
answer = str(input('Do you want to check another area? (y/n)(yes/no): '))

def script():
      restart = input("Enter the name of your city or zip code here:")
      if restart == "yes" or restart == "y":
        print (city_zip)
      if restart == "n" or restart == "no":
        print ("Thank you for checking the weather!")
      script()
###n or no will end, but y or yes will not restart


#allow the user to run the program multiple times
#Validate wheather the user entered valid data. if valid data isn't presented notify the user.
#use try blocks when establishing connections to the webservice. you must print a message to the user #indication whether or not the connection was successful.