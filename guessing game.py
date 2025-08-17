import random

print("Number Guessing Game")

# randint function to generate the random number b/w 1 to 9
number = random.randint(1, 9)
chances = 0

print("Guess a number (between 1 and 9):")

# While loop to count the number of chances
while True:

    # Enter a number between 1 to 9
    guess = int(input())

    # Compare the user entered number with the number to be guessed
    if guess == number:
        print(
            f'CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER {number} IN {chances+1} ATTEMPTS!')
        break

    # Check if the user entered number is smaller than the generated number
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    # The user entered number is greater than the generated number
    else:
        print("Your guess was too high: Guess a number lower than", guess)

    # Increase the value of chance by 1
    chances += 1
    
