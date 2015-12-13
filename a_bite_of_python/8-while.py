number = 23
running = True

while running:
    guess = int(input('Enter the number: '))

    if guess == number:
        print('You guess it!')
        running = False
    elif guess < number:
        print('Guess < Number')
    else:
        print('Guess > Number')

print('That\'s all!')