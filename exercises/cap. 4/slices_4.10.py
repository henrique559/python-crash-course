players = ['charles', 'martina', 'michael', 'florence', 'deli']

# Vai mostrar o indice zero até o indice 2 (lembre-se, n-1)
# Pode se usar -1 para pegar o ultimo item da lista e um novo valor para pular de n em n indices igualmente
# a função len()

print("The first three items in the list are: ")

for player in players[:3]:
    print(player.title())
    
print("\nThe items from the middle of the list are: ")

for player1 in players[1:4]:
    print(player1.title())
    
print("\nThe last three items in the list are: ")

for player2 in players[-3:]:
    print(player2.title())