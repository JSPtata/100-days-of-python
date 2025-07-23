import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")
choice=input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
number=random.randint(1,101)
def guess_number(count):
    while count > 0:
        print(f"You have {count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            print("Guess again.")
        elif guess < number:
            print("Too low.")
            print("Guess again.")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            return
        count -= 1
    print(f"You've run out of guesses.You lose! The number was {number}.")
if choice=='easy':
    guess_number(10)
elif choice=='hard':
    guess_number(5)
else:
    print("Invalid choice.Please restart the game.")

