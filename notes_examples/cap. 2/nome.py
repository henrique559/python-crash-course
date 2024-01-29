nome = ["pedro", "rafaella", "carlinhos", "demonio"]

nome.append(input("Digite aqui o seu nome: \n"))

for i in range(len(nome)):
    print(f"Olá {nome[i].title()}, tudo bem?")
    
    
# Adicionar itens no final da lista = append()
# Acessar o ultimo item da lista = teste[-1]