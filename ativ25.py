#juros simples
quantia = float(input("digite uma quantia para tirar o juro simples:"))
tempo = float(input("coloque o tempo da aplicação em meses: "))
indice = int(input("coloque a taxa de juros: "))

montante = (quantia*tempo*(indice/100))+quantia

print(f"o montante acumulado em {tempo:.0f} meses é {montante}")
