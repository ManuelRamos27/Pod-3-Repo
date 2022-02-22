# READ THE INSTRUCTIONS FILE (nba_challenge_instructions.md) FIRST
# EXTRA: This challenge is not required for a grade!

# print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3-pt shots made by Fred VanVleet

fred_vanvleet_3pts_made = 43
# TODO: Create variable here for number of 3-pt shots made by James Harden

james_harden_3pts_made = 37

print("Challenge 2.2:")

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3-ptoint shots")

# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3-ptoint shots")

# TODO: Create print statement here for James Harden
print()

print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3-ptoint shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3-pt shot attempts by Jamal Murray

jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109


jm = jamal_murray_3pts_attempts
fv = fred_vanvleet_3pts_attempts
jhr = james_harden_3pts_attempts 
# TODO: Create variable here for number of 3-pt shot attempts by Fred VanVleet

# TODO: Create variable here for number of 3-pt shot attempts by James Harden
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3-point shots out of Z 3-point shot attempts."
print()

print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3-ptoint shots out of {james_harden_3pts_attempts} shots attempted.")


print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`

jm_percentage_of_3pts_shots_made = 46/93
jmp = jm_percentage_of_3pts_shots_made

fv_percentage_of_3pts_shots_made = 43/110

fvp = fv_percentage_of_3pts_shots_made


jh_percentage_of_3pts_shots_made = 37/109


jmp = jh_percentage_of_3pts_shots_made
# TODO: Calculate and print the 3-point percentage for Jamal Murray
# TODO: Calculate and print the 3-point percentage for Fred VanVleet
# TODO: Calculate and print the 3-point percentage for James Harden
print()

print(f"James Harden three point percentage was {jh_percentage_of_3pts_made}.")

print(f" Fred VanVleet percentage of 3pts shot made was {fv_percentage_of_3pts_made}.")

print(f"Jamal Murray percentage of 3pts shots made was {jm_percentage_of_3pts_shots_made}.")





print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

""" to complete this challenge each line was print separately using the \n escape character. My screen is too small to see each line.
"""


print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case


""" to complete this challenge the same escapr character \n was used to print each sentence on a separate line. to print all uppercase letter the .upper method was used on the variable that stored the text."""

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this

laker_are_best = True

# TODO: print out the variable in an f-string to convey your opinion on the lakers

print(f"The lakers are the best team in the NBA {laker_are_best}.")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out.

lb = int("lakers_are_best")
print(lb)

# TODO: Convert your `lakers_are best` variable to a float, and print it out

lb_Float = float(lb)

print(lb_Float)


print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

jhp_three_point_perc = str("jhp")

#same for each player

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
jhp =int(jhp_three_point_perc)
jmp =int(jm_percentage_of_3pts_shots_made)

