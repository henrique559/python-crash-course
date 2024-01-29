user_age = int(input("Insert here your age: \n"))

if user_age < 2:
    print('You are a baby.')
elif user_age > 2 and user_age < 4:
    print('You are a toddler.')
elif user_age > 4 and user_age < 13:
    print('You are a kid.')
elif user_age > 13 and user_age < 20:
    print('You are a teenager.')
elif user_age > 20 and user_age < 65:
    print('You are an adult.')
else:
    print('You are an elder.')