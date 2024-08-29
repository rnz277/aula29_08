#as listas em python permitem adicionar tipos de dadosdeferentes
nomes = [0,"karithon", 1,"gomes", 2,"python", 3,"ia", 4,"data drive", 4.5,"prugramação"]

#retorara lista inteira
print(nomes)

#retornar um unico indice
print(nomes[0])

#para retornar o ultimo indice 
print(nomes[-1])

#retornar um intervalo da lista
print(nomes[0:2])
print(nomes[:2])
print(nomes[2:])

#para ordenar a lista
nomes.sort()
nomes.sort(reverse=True) 
print(f"lita ordenada dentro do fstring{sorted(nomes)}")

#para remover itens da lista (remove, pop, del)
nomes.remove([1])
#o comando pop guardara o numero removido será guardado em variavel
nomes.pop()
#o del remove indoces e intervalos
del nomes[]

#adicionar elementos a listas
minha_lista = [1, 2, 3]

# 1. Usando o método append()
# Adiciona o elemento ao final da lista
minha_lista.append(4)
print(minha_lista)  # Saída: [1, 2, 3, 4]

# 2. Usando o método extend()
# Adiciona os elementos de outra lista ao final da lista original
minha_lista.extend([4, 5])
print(minha_lista)  # Saída: [1, 2, 3, 4, 5]

# 3. Usando o método insert()
# Insere o elemento a um lugar especifico da lista
minha_lista.insert(1, 'a')
print(minha_lista)  # Saída: [1, 'a', 2, 3, 4, 5]

# 4. Usando o operador +
# Concatena a lista original com uma nova lista
nova_lista = minha_lista + [6, 7]
print(nova_lista)  # Saída: [1, 'a', 2, 3, 4, 5, 6, 7]