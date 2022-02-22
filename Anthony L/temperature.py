#temperature challenge

# 1. Convert a temperature of 100 degrees fahrenheit to celsius
#     * Save this to a variable called `fahrenheit_100`, and use `print()` to print out the value
#     * Is the resulting temperature you get an integer or float? How do you know?
#     * Celsius = (Fahrenheit – 32) * 5/9 
 
print() 

print ('#1')
fahrenheit_100 = 100 #1
print (f'fahrenheit degrees is {fahrenheit_100}') #1
celsius_a = (fahrenheit_100 - 32) * 5/9 #1
print (f'celsius degrees is {celsius_a}') #1
print (f'fahrenheit is {type(fahrenheit_100)}') #1
print (f'celsius is {type(celsius_a)}') #1

print ()

print ("the value 'fahrenheit_100' is an integer because it does not have a decimal point and it was hard-coded by user")
print ("the value 'celsius' is a float because the conversion comes back with a decimal point")
print ("running the (type) function also reveals the temperatures are <class 'int'> and <class 'float'>")

print()


# 2. Convert a temperature of 0 degrees fahrenheit to celsius
#     * Save this to a variable called `fahrenheit_0`, and use `print()` to print out the value

print ('#2')
fahrenheit_0 = 0 #2
print (f'fahrenheit degrees is {fahrenheit_0}') #2
celsius_b = (fahrenheit_0 - 32) * 5/9 #2
print (f'celsius degrees is {celsius_b}') #2
# print (f'fahrenheit is {type(fahrenheit_0)}') #2
# print (f'celsius is {type(celsius_b)}') #2

print()


# 3. Convert a temperature of 34.2 degrees fahrenheit to celsius
#     * Do this one all in one print statement **without** saving any variables

print ('#3')
print (f'A temperature of 34.2 degrees Fahrenheit is equal to {(34.2 - 32) * 5/9} degrees Celsius')

print()


# 4. Convert a temperature of 5 degrees celsius to fahrenheit?
#    * Fahrenheit = (Celsius * 9/5) + 32

print ('#4')
celsius_5 = 5 #4
print (f'celsius degrees is {celsius_5}') #4
fahrenheit_a = (celsius_5 * 9/5) + 32 #4
print (f'fahrenheit degrees is {fahrenheit_a}') #4

print ()


# 5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?

print ('#5')
celsius_30 = 30.2 #5
fahrenheit_85 = 85.1 #5
print (f'celsius degrees is {celsius_30}') #5
print (f'fahrenheit degrees is {fahrenheit_85}') #5
print (f'A temperature of 30.2 degrees Celsius is equal to {(30.2 * 9/5) + 32} degrees Fahrenheit') #5
print ('A temperature of 30.2 degrees Celsius is hotter than a temperature of 85.1 degrees Fahrenheit') #5

print()