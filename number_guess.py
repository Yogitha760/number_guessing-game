# number_guess.py

import random

def main():
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    # Allow the user up to 3 guesses
    for attempt in range(3):
        try:
            # Ask the user to guess the number
            guess = int(input("Guess a number: "))
            
            # Check if the guess is correct
            if guess == number:
                print("Congratulations! You guessed the number correctly.")
                break
            else:
                if attempt < 2:  # Provide feedback if not the last attempt
                    print("Incorrect guess. Try again!")
                else:  # Inform the user if it's the last attempt
                    print(f"Sorry, the number was {number}. Better luck next time!")
        except ValueError:
            print("Please enter a valid integer.")
            
if __name__ == "__main__":
    main()
  
