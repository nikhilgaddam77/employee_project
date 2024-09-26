import random

def number_guessing_game():
    """
    Creates a number guessing game where the user tries to guess a randomly
    generated number within a specified range.

    Returns:
        None
    """

    min_value = 1
    max_value = 100
    attempts = 0

    print(f"I'm thinking of a number between {min_value} and {max_value}.")

    random_number = random.randint(min_value, max_value)

    while True:
        try:
            guess = int(input("Take a guess: "))

            if guess < min_value or guess > max_value:
                print(f"Please enter a number between {min_value} and {max_value}.")
            elif guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                attempts += 1
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()