print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.

Go through the dictionary and print out the following 3 pieces of information about the restaurant:
1. The latitude and longitude of Four Barrel Coffee
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print(f"Four Barrel Coffee\nLatitude:{restaurant['latitude']}\nLongitude:{restaurant['longitude']}\n")
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
Four_Barrel_Coffee_Address = f"Four Barrel Coffee Address:\n{restaurant['address1']},\n{restaurant['city']},{restaurant['state']}\n{restaurant['zip_code']}"
print(Four_Barrel_Coffee_Address)
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print({restaurant['url']})





# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary
fav_nyc_rest1 = {
    "name":'Veggie Castle',
    "address":'132-09 Liberty Ave, South Richmond Hill, NY 11419',
    "favourite_dish":'Mac & Cheese'
}
fav_nyc_rest2 = {
    "name":'Jerrells BETR BRGR',
    "address":'117 6th Ave, New York, NY 10013',
    "favourite_dish":'O.G Betr Brgr',
}
fav_nyc_rest3 = {
    "name":'Modern Love',
    "address":'317 Union Avenue, Brooklyn, NY 11211',
    "favourite_dish":'Bucatini a la Vodka'
}
print(f"{fav_nyc_rest1}\n{fav_nyc_rest2}\n{fav_nyc_rest3}")
# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich"
}
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
fav_nyc_rest1.pop('favourite_dish')
print(fav_nyc_rest1)

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address.
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.
fav_nyc_rest2["address"]='116th & Broadway, NY 10016'
print(fav_nyc_rest2["address"])
print(fav_nyc_rest2)


print("Question 5")
'''
Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
'''

# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
# TODO: Loop through your list and print out the name and address of each restaurant
restaurants = [fav_nyc_rest1,fav_nyc_rest2,fav_nyc_rest3]
for i in restaurants:
    print({i['name']},{i['address']})