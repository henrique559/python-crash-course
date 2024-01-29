motorcycles = ["honda", "yamaha", "suzuki"]
# motorcycles.insert(2, "subaru")
# Não substitui o item da lista, coloca todos a direita.
print(motorcycles)


# Sintaxe - função insert():
# nome_teste.insert(qntd, "oque desejar")
# '''

# Função del - deleta o item da lista, caso saiba sua posição, ex:
# del lista[indice]
# del motorcycles[2]
# print(motorcycles) 

# input()
# motorcycles.append('motoca')
# print(motorcycles)
# append() = insere o item ao final da lista
# insert() = insere o item na posição que o usuario escolher e move o item localizado nessa posição pro lado direito.

# del = deleta o item em tal posição ou a lista inteira
# pop() = remove o item da posição final da lista igualmente o 'del', porém, pode reutilizar esse item removido para mover em outras listas ou jogar em alguma variavel.
# > Pode ser importante para remover coisas de listas com datas cronologicas ou já organizadas.
# recebe como argumentos a posição de tal item da lista, caso queira retirar esse item de qualquer posição que esteja, não apenas no final.
# Ex: motorcycles.pop(num)

# Se você quer deletar algo e não se importa com esse valor, use 'del'
# Caso queira reutilizar esse valor deletado para outra coisa, como por exemplo uma lista de 'usuarios removidos', use 'pop()'

# old_motorcycles = motorcycles.pop(1)
# print(motorcycles)
# print(old_motorcycles)

# remove() = deleta o item sem precisar saber a posição dele na lista, somente o nome que está na lista ou inserindo uma variavel com string contendo esse nome.
#

too_expensive = 'honda'

motorcycles.remove(too_expensive)
print(f"I removed {too_expensive} because it's too expansive.")
print(motorcycles)