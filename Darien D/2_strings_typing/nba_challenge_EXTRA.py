# READ THE INSTRUCTIONS FILE (nba_challenge_instructions.md) FIRST
# EXTRA: This challenge is not required for a grade!

# print("Challenge 2.1:")
from pickle import FALSE


jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3-pt shots made by Fred VanVleet
# TODO: Create variable here for number of 3-pt shots made by James Harden
Fred_VanVleet_3pts_made = 191 #As of 2/11/22 2021-2022 season
James_Harden_3pts_made = 102 #As of 2/11/22 2021-2022 season

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3-ptoint shots")
# TODO: Create print statement here for Fred VanVleet
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, Fred VanVleet made {Fred_VanVleet_3pts_made} 3-ptoint shots")
print(f"In the 2020 NBA playoffs, James Harden made {James_Harden_3pts_made} 3-ptoint shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3-pt shot attempts by Jamal Murray
# TODO: Create variable here for number of 3-pt shot attempts by Fred VanVleet
# TODO: Create variable here for number of 3-pt shot attempts by James Harden
jamal_murray_3pts_attempted = 98 #made up
Fred_VanVleet_3pts_attempted = 430 #As of 2/11/22 2021-2022 season
James_Harden_3pts_attempted = 307 #As of 2/11/22 2021-2022 season



print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3-point shots out of Z 3-point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3-point shots out of {jamal_murray_3pts_attempted} 3-point shot attempts.\n")
print(f"In the 2020 NBA playoffs, Fred VanVleet  made {Fred_VanVleet_3pts_made} 3-point shots out of {Fred_VanVleet_3pts_attempted} 3-point shot attempts.\n")
print(f"In the 2020 NBA playoffs, James Harden made {James_Harden_3pts_made} 3-point shots out of {James_Harden_3pts_attempted} 3-point shot attempts.\n")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player\n")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3-point percentage for Jamal Murray
# TODO: Calculate and print the 3-point percentage for Fred VanVleet
# TODO: Calculate and print the 3-point percentage for James Harden
print(f"In the 2020 NBA playoffs, Jamal Murray had {jamal_murray_3pts_made /jamal_murray_3pts_attempted} 3-point shot percentage.\n ")
print(f"In the 2020 NBA playoffs, Fred VanVleet had {Fred_VanVleet_3pts_made /Fred_VanVleet_3pts_attempted} 3-point shot percentage.\n ")
print(f"In the 2020 NBA playoffs, James Harden had {James_Harden_3pts_made /James_Harden_3pts_attempted} 3-point shot percentage.\n ")
print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print(f"In the 2020 NBA playoffs, Jamal Murray had {jamal_murray_3pts_made /jamal_murray_3pts_attempted} 3-point shot percentage.\n ")
print(f"In the 2020 NBA playoffs, Fred VanVleet had {Fred_VanVleet_3pts_made /Fred_VanVleet_3pts_attempted} 3-point shot percentage.\n ")
print(f"In the 2020 NBA playoffs, James Harden had {James_Harden_3pts_made /James_Harden_3pts_attempted} 3-point shot percentage.\n ")
print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case
print(f"In the 2020 NBA playoffs, Jamal Murray had {jamal_murray_3pts_made /jamal_murray_3pts_attempted} 3-point shot percentage.\n ".upper())
print(f"In the 2020 NBA playoffs, Fred VanVleet had {Fred_VanVleet_3pts_made /Fred_VanVleet_3pts_attempted} 3-point shot percentage.\n ".upper())
print(f"In the 2020 NBA playoffs, James Harden had {James_Harden_3pts_made /James_Harden_3pts_attempted} 3-point shot percentage.\n ".upper())
print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = False
print(f"The statement that the lakers are the best team in the NBA is {lakers_are_best}")
print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out.
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(int(lakers_are_best))
lakers_are_best=(int(lakers_are_best))
print(type(lakers_are_best))
lakers_are_best=(float(lakers_are_best))
print(float(lakers_are_best))
print(type(lakers_are_best))


print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
jamal_murray_3pts_percentage=str(jamal_murray_3pts_made /jamal_murray_3pts_attempted)
James_Harden_3pts_percentage=str(James_Harden_3pts_made /James_Harden_3pts_attempted)
Fred_VanVleet_3pts_percentage=str(Fred_VanVleet_3pts_made /Fred_VanVleet_3pts_attempted)

print(type(jamal_murray_3pts_percentage))
print(type(James_Harden_3pts_percentage))
print(type(Fred_VanVleet_3pts_percentage))

print(f"In the 2020 NBA playoffs, Jamal Murray had {jamal_murray_3pts_percentage} 3-point shot percentage.\n ".upper())
print(f"In the 2020 NBA playoffs, Fred VanVleet had {Fred_VanVleet_3pts_percentage} 3-point shot percentage.\n ".upper())
print(f"In the 2020 NBA playoffs, James Harden had {James_Harden_3pts_percentage} 3-point shot percentage.\n ".upper())

jamal_murray_3pts_percentage=float(jamal_murray_3pts_made /jamal_murray_3pts_attempted)
James_Harden_3pts_percentage=float(James_Harden_3pts_made /James_Harden_3pts_attempted)
Fred_VanVleet_3pts_percentage=float(Fred_VanVleet_3pts_made /Fred_VanVleet_3pts_attempted)
print(type(jamal_murray_3pts_percentage))
print(type(James_Harden_3pts_percentage))
print(type(Fred_VanVleet_3pts_percentage))

print(f"In the 2020 NBA playoffs, Jamal Murray had {jamal_murray_3pts_percentage} 3-point shot percentage.\n ".upper())
print(f"In the 2020 NBA playoffs, Fred VanVleet had {Fred_VanVleet_3pts_percentage} 3-point shot percentage.\n ".upper())
print(f"In the 2020 NBA playoffs, James Harden had {James_Harden_3pts_percentage} 3-point shot percentage.\n ".upper())