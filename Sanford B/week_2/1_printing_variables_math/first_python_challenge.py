from os import lseek


#print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal = 'This evening I had salmon, spinach, and sweet potatoes for dinner.'

#print('1.2: Print the meal variable')
print(meal)

#print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal = 'I would like to have fried chicken with macaroni n cheese for dinner'
print(meal)

print('2: How old is Google?')
# 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# to figure out how old Google is
# ex: my_age = current_year - birth_year
google_age = 2022 - 1993 
print (google_age) 

# 2.2: Print out a sentence about Google's age. Make sure to include your variable in the f-string!
how_old_google_turns = f'Google was founded in 1993, which means google turns {google_age} this year'
print(how_old_google_turns)



# 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# then print the info.
# (Assume 12 months for each year, you don't need to check which month they started)
google_age_months = 29 * 12
google_newage = f'Google turns {google_age_months} months today.'
print(google_newage)


#print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
#print('Fix the problem and turn the comment back into regular Python code')
completion_message = 'Completed the first Python challenge'


# 3.2 What were the syntax errors that you fixed? print out a quick explanation of each one.
cyntex_errors = 'The syntex error was caused by a space between cyntex and error. Python does not allow spaces when assigning a variable. Also text was missing quotation marks arround the message '
#print('3.3: Turn the comment below back into regular Python code')
print(cyntex_errors)
#print(completion_message)
print(completion_message)