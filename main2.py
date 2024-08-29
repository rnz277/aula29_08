# tipos de contatenação
# concatenação com sinal(+)
num = int(input("digite um numero inteiro: "))

# não possivel concatenar numero inteiro usanso esse metodo, 
# a menos que o converta o n umero inteiro em estring
print("ola,"+ str(num)+"seja bem vindo")
print(type(num))

#concatenação com a (,)
print("o numero é: ",num)

#concatenação com fstring (f)
print(f"o numero digitado é: {num} usando a contatenção f")

div = num/3
# usando format(f)para formatação de números
# limitando a quantidade de casas decimais
print(f"o resultado da divisão é: {div:.2f}")