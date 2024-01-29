my_pizzas = ['shimeji', 'frango com catupiry', 'calabresa']

friend_pizzas = my_pizzas[:]

my_pizzas.append("queijo")
friend_pizzas.append("chocolate")

print("My favorite pizzas are: ")

for pizza1 in my_pizzas:
    print(pizza1.title())
    
print("\nMy friend's favorite pizzas are: ")

for pizza2 in friend_pizzas:
    print(pizza2.title())
    
    