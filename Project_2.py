# This will be a project that creates a mini game to let the user pick a number between 1 and 1000. if the users number is higher than the selected number, they will be prompted to pick a lower number vice versa.

import random
goal = random.randint(1, 1000)
#print(goal)  # This line is for debugging purposes; it shows the selected number.
#Instructions
print("Your goal is to find the number between 1 and 1000 that the computer has selected.")
print("")
#Program Start
user_guess = int(input("Please enter your guess: "))
while user_guess != goal:
    if user_guess > goal: #Scenario 1, user's guess is too high
        print("Your guess is too high. Try again.")
        
    if user_guess < goal: #Scenario 2, user's guess is too low
        print("Your guess is too low. Try again.")

    if user_guess == goal: #Scenario 3, user's guess is correct
        break
    
    if user_guess < 1 or user_guess > 1000: #Scenario 4, Uuer's guess is out of range
        print("Invalid input. Please enter a number between 1 and 1000.")

   
    if not isinstance(user_guess, int): #Scenario 5, user's input is not an integer
        print("Invalid input. Please enter a valid integer between 1 and 1000.")
        user_guess = int(input("Please enter your guess: "))
        continue

    print("") #After a scenario, Start again
    user_guess = int(input("Please enter your guess: "))


#This prints after the user has guessed the number correctly.
print("Congratulations! You guessed the number correctly.")