import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")

choice=input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
number=random.randint(1,100)

def guess_number(attempts):
    while attempts > 0:
        print(f"You have {count} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            return
        attempts -= 1
        print("Guess again.")
        
    print(f"You've run out of guesses.You lose! The number was {number}.")
    
if choice=='easy':
    guess_number(10)
elif choice=='hard':
    guess_number(5)
else:
    print("Invalid choice.Please restart the game.")

