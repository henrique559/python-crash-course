import os 
invite = ["pedro", "rafaella", "carlinhos", "luci"]

os.system("clear")

for i in range(len(invite)):
    print(f"Olá {invite[i].title()}, gostaria de te convidar para ir em um jantar comigo.")
    
input()
os.system("clear")

print(f"(Infelizmente, o {invite[2].title()} não irá conseguir comparecer no jantar.)\n")
invite[2] = "jesus"

for i in range(len(invite)):
    print(f"Olá {invite[i].title()}, gostaria de te convidar para ir em um jantar comigo.")
    

print(f"você convidou {len(invite)} pessoas para o jantar")
    
input()
os.system("clear")

# Sempre use -1 para acessar o ultimo item de uma lsita.