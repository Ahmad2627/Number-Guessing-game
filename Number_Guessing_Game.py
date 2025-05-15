# # We are going to write a program that generates a random number and asks the user to 
# # guess it. 
# # If the player’s guess is higher than the actual number, the program displays “Lower 
# # number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# # number please” When the user guesses the correct number, the program displays the 
# # number of guesses the player used to arrive at the number. 
# ====================================================================================
import random

def guess_game():
    number_to_guess = random.randint(1,100)
    
    print("Welcome to the Number guessing game!")
    print("I selected a number from 0 to 100, now you have to guess it under 6 turns....")
    
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