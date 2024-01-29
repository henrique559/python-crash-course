alien_color = ['green', 'red', 'yellow']

user_input = input('Guess a color: ').lower()

if user_input == 'green':
    print('You earned 5 points.')
elif user_input == 'yellow':
    print('You earned 10 points.')
elif user_input == 'red':
    print('You earned 15 points.')
else:
    print('You failed!')