import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("=" * 40)
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"\n🎉 Congratulations! You guessed it right!")
            print(f"The number was {number_to_guess}.")
            print(f"It took you {attempts} attempt(s).")
            break

if __name__ == "__main__":
    number_guessing_game()