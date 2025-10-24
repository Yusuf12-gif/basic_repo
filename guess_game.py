import random

def guess_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Choose difficulty: easy (10 tries) / hard (5 tries)")
    difficulty = input("Type 'easy' or 'hard': ").lower()
    
    attempts = 10 if difficulty == 'easy' else 5
    number = random.randint(1, 100)
    
    while attempts > 0:
        guess = int(input(f"\nYou have {attempts} attempts left. Make a guess: "))
        if guess == number:
            print(f"✅ Correct! The number was {number}. You win!")
            return
        elif guess < number:
            print("🔼 Too low!")
        else:
            print("🔽 Too high!")
        attempts -= 1
    
    print(f"❌ You've run out of guesses! The number was {number}.")

if __name__ == "__main__":
    guess_game()
