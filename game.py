import random

def play_game():
    print("=" * 40)
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯")
    print("=" * 40)
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random integer between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

    while attempts < max_attempts:
        try:
            # Get the user's guess and convert it to an integer
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            # Handle cases where user types text or symbols instead of a number
            print("❌ Invalid input! Please enter a whole number.\n")
            continue
            
        attempts += 1
        
        # Check the user's guess against the secret number
        if guess < secret_number:
            print("📈 Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("📉 Too high! Try a lower number.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
            return
            
    print(f"💥 Game Over! You've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    while True:
        play_game()
        # Ask the player if they want to try again
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != 'yes' and again != 'y':
            print("\nThanks for playing! Goodbye! 👋")
            break

