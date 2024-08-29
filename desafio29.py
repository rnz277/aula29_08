#o valor das variaveis.
distancia_percorrida = float(input('Digite a distancia percorrida: '))
conbustivel = float(input('Digite o conbustivel gasto: '))

#exprimido a taxa de conversão.
taxa_conversão = distancia_percorrida/conbustivel

#o consumo medio é igual o resultado da taxa de conversão.
consumo_medio = taxa_conversão

#resultado final.
print(f'O consumo medio é igual a: {consumo_medio}')