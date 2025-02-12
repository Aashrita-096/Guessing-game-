import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Allow user to set the range
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    
    if lower_bound >= upper_bound:
        print("Invalid range! Lower bound must be less than upper bound.")
        return
    
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = int((upper_bound - lower_bound) / 2) + 3  # Dynamic max attempts
    
    print(f"I have selected a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                return
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
