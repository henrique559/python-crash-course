players = ['charles', 'martina', 'michael', 'florence', 'deli']

# Vai mostrar o indice zero até o indice 2 (lembre-se, n-1)
# Pode se usar -1 para pegar o ultimo item da lista e um novo valor para pular de n em n indices igualmente
# a função len()

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())