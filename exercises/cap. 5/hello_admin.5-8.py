usernames = ['carlinhos', 'admin', 'rafaella', 'pedro', 'jotaro']

for name in usernames:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")