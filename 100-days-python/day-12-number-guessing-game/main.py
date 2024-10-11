#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

if __name__ == "__main__":
    print(logo)
    intro = "Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.\n"
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guess_limit = 0
    if (difficulty == 'easy'):
        guess_limit = 10
    else:
        guess_limit = 5

    user_guess = 0
    status = "continue" # win, lose, continue
    
    while (guess_limit > 0 and status == "continue"):
        print(f'Your have {guess_limit} attempts remaining to guess the number.')
        user_guess = int(input('Make a guess: '))
        if (user_guess > number):
            print('Too high.')
        elif (user_guess < number):
            print('Too low.')
        else:
            print("You're correct!")
            status = "win"
        guess_limit -= 1
        if (guess_limit <= 0 and status == 'continue'):
            print('You have run out of guesses, you lose.')
            status = 'lose'


    


