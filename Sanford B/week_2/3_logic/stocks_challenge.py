print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client_name = input('What is your name? ')
# TODO: Write code to ask the client his savings and save it to another variable.
Client_saving = input('How much do you have to invest')
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

Client_saving = int(Client_saving)
print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn':
    print(f'You can buy (Client_saving / amazon) shares of Amazon.')
elif stock == 'aapl': 
    print(f'You can buy {Client_saving / apple} shares of Apple.')
elif stock == 'fb':
    print(f'You can buy {Client_saving / fb} shares of Facebook.')    
elif stock == 'goog':
     print(f'You can but {Client_saving / google} shares of Google')   
elif stock == 'msft':
    print(f'You can buy {Client_saving / msft} shares of Microsoft')
else:
    print('Please, enter one of the stocks listed above')
'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
if stock == 'amzn':
    print(f'{client_name} has ${Client_saving}and can buy {(Client_saving / amazon)} shares of Amazon at the current price of ${amazon}.')
elif stock == 'aapl':
    print(f'{client_name} has ${Client_saving}and can buy {(Client_saving / apple)} shares of Amazon at the current price of ${apple}.')
elif stock == 'fb':
    print(f'{client_name} has ${Client_saving}and can buy {(Client_saving /fb)} shares of Amazon at the current price of ${fb}.')
elif stock == 'goog':
    print(f'{client_name} has ${Client_saving}and can buy {(Client_saving / google)} shares of Amazon at the current price of ${google}.')
elif stock == 'msft':
    print(f'{client_name} has ${Client_saving}and can buy {(Client_saving / msft)} shares of Amazon at the current price of ${msft}.')
else:
    print('Please, enter one of the stocks listed above.')
print()
