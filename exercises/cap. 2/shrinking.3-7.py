import os 
invites = ["pedro", "rafaella", "carlinhos", "luci"]

os.system("clear")
print("(Convites para jantar)\n")

for i in range(len(invites)):
    print(f"Olá {invites[i].title()}, gostaria de te convidar para ir em um jantar comigo.")
    
input()
os.system("clear")

print(f"(Infelizmente, o {invites[2].title()} não irá conseguir comparecer no jantar, outra pessoa vai substituir seu lugar)\n")
invites[2] = "dalva"

for i in range(len(invites)):
    print(f"Olá {invites[i].title()}, gostaria de te convidar para ir em um jantar comigo.")
    
input()
os.system("clear")

print('''Olá novamente, encontramos uma mesa maior no restaurante e 
      gostariamos de convidar novas pessoas\n''')

invites.insert(0, "cleide")
invites.insert(2, "jesus")
invites.append("shinji")

for qntd in range(len(invites)):
    print(f"Olá {invites[qntd].title()}, gostaria de te convidar para ir em um jantar comigo.")

input()
os.system("clear")

print("(Infelizmente, a mesa maior não chegará a tempo no restaurante, portanto temos que retirar alguns nomes da lista)\n")

i = (len(invites) - 1)
while(i > 1):
    removed_invites = invites.pop(i)
    i -= 1
    print(f"Infelizmente, {invites[i].title()} não será convidado")

input()
os.system("clear")

print("Novos convites: \n")
for ii in range(len(invites)):
    print(f"Olá {invites[ii].title()}, gostaria de te convidar para ir em um jantar comigo.")
    
input()
os.system("clear")

del invites[0]
print(f"Lista vazia")



