my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
for foods in my_foods:
    print(foods.title())
    
    
print("\nMy Friend's favorite foods are: ")
for foods2 in friend_foods:
    print(foods2.title())
# Usar slice para copiar listas.
