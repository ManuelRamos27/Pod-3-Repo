print()

print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon_price = 3000
apple_price = 100
facebook_price = 250
google_price = 1400
microsoft_price = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.

client = input('Enter client name: ')

# TODO: Write code to ask the client his savings and save it to another variable.

savings = int(input('Enter client savings: '))


# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. ")
print()


# print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

if stock == 'amzn':
    price = amazon_price
    shares = savings / price
elif stock == 'aapl':
    price = apple_price
    shares = savings / price
elif stock == 'fb':
    price = facebook_price
    shares = savings / price
elif stock == 'goog':
    price = google_price
    shares = savings / price
elif stock == 'msft':
    price = microsoft_price
    shares = savings / price
else: 
    print('Please enter one of the stocks listed above.')  

print()


# '''
# Your code should look like this:

# if stock == "amzn":
#     ...
# elif ...
# else ...
# '''


print("Challenge 3.2.3: Output for the user the result")

print()

# # TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client.
# # Result should be in a format like this:

# # Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.


if stock == 'amzn':
    print (f'{client} has ${savings} in savings and they can buy {shares} shares of {stock} at the current price of ${price} per stock')
elif stock == 'aapl':
    print (f'{client} has ${savings} in savings and they can buy {shares} shares of {stock} at the current price of ${price} per stock')
elif stock == 'fb':
    print (f'{client} has ${savings} in savings and they can buy {shares} shares of {stock} at the current price of ${price} per stock')
elif stock == 'goog':
    print (f'{client} has ${savings} in savings and they can buy {shares} shares of {stock} at the current price of ${price} per stock')
elif stock == 'msft':
    print (f'{client} has ${savings} in savings and they can buy {shares} shares of {stock} at the current price of ${price} per stock')

print()

# amzn = 'Amazon'
# aapl = 'Apple'
# fb = 'Facebook'
# goog = 'Google'
# msft ='Microsoft'
