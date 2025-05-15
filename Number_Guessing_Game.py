# Number Guessing Game
# This is a simple number guessing game where the user has to guess a number between 1 and 100.
import random

def guess_game():
    number_to_guess = random.randint(1,100)
    
    print("Welcome to the Number guessing game!")
    print("I selected a number from 1 to 100, now you have to guess it under 6 turns....")

    guess = None
    attempts = 0
    
    while guess != number_to_guess:
        try:
            guess = int(input("Enter a number to guess: "))
            if attempts == 5:
                print(f"\nThe number is {number_to_guess}. Better Luck Next Time.")
                break
            attempts += 1
            
            if guess < number_to_guess:
                print("Your number is Smaller ....")
                
            elif guess > number_to_guess:
                print("Your number is Bigger  ...")
                
            else:
                print(f"Congratulations! You guessed the {number_to_guess} in {attempts}attempts.")
                
        except ValueError:
            print("Invalid number! Try to enter an other number.")
            
guess_game()