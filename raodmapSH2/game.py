import random
import time

def choose_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        return 10  # Easy: 10 chances
    elif choice == 2:
        return 5   # Medium: 5 chances
    elif choice == 3:
        return 3   # Hard: 3 chances
    else:
        print("Invalid choice. Defaulting to Medium (5 chances).")
        return 5

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Pilih tingkat kesulitan
    chances = choose_difficulty()
    print(f"\nYou have {chances} chances to guess the correct number.\n")

    # Pilih angka acak
    number_to_guess = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while chances > 0:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == number_to_guess:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"It took you {elapsed_time} seconds to guess correctly.")
            return  # Game over, user won

        elif guess < number_to_guess:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")
        
        chances -= 1
        print(f"You have {chances} chances left.\n")

    print(f"Sorry! You've run out of chances. The correct number was {number_to_guess}.")

def main():
    while True:
        play_game()

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

