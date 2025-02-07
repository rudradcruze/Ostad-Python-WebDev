# Guess the number game
secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts = attempts + 1
    
    if guess == secret_number:
        print(f"You got it in {attempts} tries! 🎉")
        break
    elif guess > secret_number:
        print("Too high! Try again!")
    else:
        print("Too low! Try again!")