cars = ['bmw', 'audi', 'toyota', 'subaru', 'volkswaggen']

# print('''função sort(): organiza automaticamente a lista em ordem alfabética de forma permanente.''')
# cars.sort()
# print(cars)

# print('''pode inverter a ordem da lista usando sort(reverse=True)''')
# cars.sort(reverse=True)
# print(cars)

# print('''Para poder organizar uma lista de forma temporaria, podemos utilizar a função sorted sorted()''')

# print(f"\nAqui está a lista original: \n{cars}")
# print(f"\nAqui está a lista organizada: \n{sorted(cars)}")
# print(f"\nAqui está a lista original novamente: \n{cars}")

# # A função sorted() também aceita o argumento 'reverse=True')

print('''Podemos inverter a lista de forma cronologica, sendo assim, os primeiros valores
      da lista serão os últimos, e os últimos valores seráo os primeiros.''')

print(f'Antes:\n{cars}')

print("\nDepois:")
cars.reverse()
print(f"{cars}")

print('''A processo de inverter é permanente, caso queira colocar na posição
      original, apenas use a função novamente.''')

# Para checar o comprimento de uma lista, use len().