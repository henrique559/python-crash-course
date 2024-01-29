favorite_fruits = ['banana', 'apple', 'orange']

user_input = input('Insert here a name of a fruit!\n').lower()

if user_input in favorite_fruits:
    print(f'You really like {user_input.title()}!')
else:
    print(f'eww... i dont like {user_input.title()}')