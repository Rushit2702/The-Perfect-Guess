import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess_count = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Get user's guess
            user_guess = int(input("Enter your guess: "))
            guess_count += 1

            if user_guess > number_to_guess:
                print("Lower number please.")
            elif user_guess < number_to_guess:
                print("Higher number please.")
            else:
                print(f"Congratulations! You guessed the number {user_guess} in {guess_count} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()