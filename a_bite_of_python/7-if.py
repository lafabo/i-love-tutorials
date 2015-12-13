number = 23
guess = int(input('Enter the number: '))

if guess == number:
    print("You guess it!")
elif guess > number:
    print("Guess > Number")
elif guess < number:
    print("Guess < Number")

print('That\'s all')