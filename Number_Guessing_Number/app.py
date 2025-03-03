import random

print("🎉 Welcome to the Number Guessing Game! 🎉\n🤔 Guess a number between 50 and 100\n🔢 You have 5 chances to guess the number!")

chances: int = 5
guess_counter: int = 0
number_to_guess = random.randrange(50, 100)

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("👉 Enter a number: "))

    if my_guess == number_to_guess:
        print(f"🎯 Yay! The number is {number_to_guess} and you found it right in the {guess_counter} attempt! 🏆")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"😞 Oops, sorry! The number was {number_to_guess}. Better luck next time! 🍀")
    elif my_guess > number_to_guess:
        print("📉 Your guess is too high! Try again ⬇️")
    elif my_guess < number_to_guess:
        print("📈 Your guess is too low! Try again ⬆️")
