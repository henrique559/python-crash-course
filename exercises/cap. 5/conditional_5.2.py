username_database = ['carlinhos', 'dalva', 'cleide', 'talita', 'rafaella', 'pedro']

user = input("Digite o seu nome de usuário: \n")

if user.lower() in username_database:
    print("Esse nome já foi selecionado, tente novamente.")
else:
    print("Bem-vindo ao Carlinhos World")