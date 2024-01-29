current_users = ['CarlinHos', 'Rafaella1', 'JesuscristO','dalva','pedro','naosei']
new_users = ['carlinhos', 'indio_emo_bombado', 'jesuscristo', 'moises','sidnei']

lowercase_users = []

for i in range(len(current_users)):
    lowercase_users.append(current_users[i].lower())

for names in new_users:
    if names in lowercase_users:
        print(f"This username is unavailable, {names}")
    else:
        print(f"This username is available, {names}")