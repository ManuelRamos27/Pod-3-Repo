print("\nChallenge: Favourite Restaurants")

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

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.

print(f'\nThe latitude of Four Barrel Coffee is: {restaurant["latitude"]} \nThe longitude of Four Barrel Coffee is : {restaurant["longitude"]}')
print(f'\n{restaurant["name"]} is located at: {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]}, {restaurant["zip_code"]}, {restaurant["country"]}')
print(f'\nTheir website is: {restaurant["url"]}')
# the lines of code above display latitude & longitude of the restaurant, as well as the address and website 
print()

print("\nQuestion 2")

print()


# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

restaurant_1  = {
    "name": "Chipotle",
    "address" : "350 5th Ave, NY 10118",
    "favourite_dish" : "Chicken Burrito"
}

restaurant_2  = {
    "name": "Qdoba",
    "address" : "61-40 188th St, NY 11365",
    "favourite_dish" : "Pulled Pork Burrito"
}

restaurant_3  = {
    "name": "Bon Chon",
    "address" : "325 5th Ave, NY 10016",
    "favourite_dish" : "Fried Chicken"
}
# The three dictionaries above contain my 3 favorite restaurants

# TODO: Print each dictionary

print(restaurant_1)
print()
print(restaurant_2)
print()
print(restaurant_3)
print()
# These lines of code will display my 3 favorite restaurants

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich"
}
'''

print("\nQuestion 3\n")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

restaurant_1.pop ('favourite_dish')
print(restaurant_1)
# This line removes the favorite dish from the dictionary

print()

print("\nQuestion 4\n")
'''
Imagine that another one of your most favourite restaurants modified its address.
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.

restaurant_1['address'] = '100 Bank Street, NY 10014'

print(restaurant_1)
print()
# The two lines of code above change and display the updated address of the restaurant

print("\nQuestion 5\n")

'''
Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
'''

# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
# TODO: Loop through your list and print out the name and address of each restaurant

restaurants = [restaurant_1, restaurant_2, restaurant_3]
for r in restaurants:
    print(r['name'], r['address'])
# This loop funciton prints all 3 restaurants in the dictionaries in the list

# END CHALLENGE


