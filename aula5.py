# Criando uma lista com diferentes tipos de dados
minha_lista = [1, "texto", 3.14, True]

# 1. Acessando elementos da lista
print(minha_lista)        # Retorna toda a lista: [1, "texto", 3.14, True]
print(minha_lista[0])     # Retorna o primeiro elemento: 1
print(minha_lista[-1])    # Retorna o último elemento: True

# 2. Fatiando a lista (retorna sublistas)
print(minha_lista[1:3])   # Retorna elementos do índice 1 ao 2: ["texto", 3.14]
print(minha_lista[:2])    # Retorna os dois primeiros elementos: [1, "texto"]
print(minha_lista[2:])    # Retorna do índice 2 até o final: [3.14, True]

# 3. Adicionando elementos à lista
minha_lista.append(42)    # Adiciona 42 ao final da lista
print(minha_lista)        # Saída: [1, "texto", 3.14, True, 42]

minha_lista.extend([7, 8])# Adiciona múltiplos elementos ao final da lista
print(minha_lista)        # Saída: [1, "texto", 3.14, True, 42, 7, 8]

minha_lista.insert(1, 'novo') # Insere "novo" no índice 1
print(minha_lista)        # Saída: [1, 'novo', "texto", 3.14, True, 42, 7, 8]

# 4. Removendo elementos da lista
minha_lista.remove('texto')  # Remove a primeira ocorrência de "texto"
print(minha_lista)           # Saída: [1, 'novo', 3.14, True, 42, 7, 8]

elemento_removido = minha_lista.pop()  # Remove e retorna o último elemento
print(elemento_removido)     # Saída: 8
print(minha_lista)           # Saída: [1, 'novo', 3.14, True, 42, 7]

del minha_lista[2]           # Remove o elemento no índice 2
print(minha_lista)           # Saída: [1, 'novo', True, 42, 7]

# 5. Ordenando a lista
numeros = [4, 2, 9, 1]
numeros.sort()               # Ordena a lista em ordem crescente
print(numeros)               # Saída: [1, 2, 4, 9]

numeros.sort(reverse=True)   # Ordena a lista em ordem decrescente
print(numeros)               # Saída: [9, 4, 2, 1]

# 6. Outras operações comuns
lista_concatenada = minha_lista + numeros  # Concatena duas listas
print(lista_concatenada)       # Saída: [1, 'novo', True, 42, 7, 9, 4, 2, 1]

lista_repetida = numeros * 2   # Repete a lista
print(lista_repetida)          # Saída: [9, 4, 2, 1, 9, 4, 2, 1]
