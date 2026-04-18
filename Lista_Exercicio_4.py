"""
Como já vimos, programação é prática! 
Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e reforçar ainda mais seu 
aprendizado e o conteúdo da vez são listas, blocos de repetição e try except. 
Bora praticar?

Exercícios:
"""

# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nomes = ['John', 'Mike', 'Bob', 'Steve']

anos = [1500, 2026]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for nome in nomes:
    print(nome)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma_impar = 0

for numero in numeros:
    if numero % 2 != 0:
        soma_impar += numero

print(f"A soma dos números ímpares de 1 a 10 é: {soma_impar}")

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for numero in reversed(numeros):
    print(numero)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, 
#    indo de 1 a 10.

numero = int(input("Digite um número: "))

for x in range(1, 11):
    print(f"{numero} * {x} = {numero * x}")

#6 - Solicite ao usuário uma lista de números separados por vírgula e utilize um bloco try-except para
#    converter cada entrada em um número inteiro. Imprima os números convertidos ou uma mensagem de erro
#    caso alguma entrada não seja um número válido. 

encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')  

try:
    for num in encomendas:
        print(int(num))
except ValueError:
    print("Uma das entradas não é um número válido.")

# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

#valores = [10, 20, 30, 40, 50]      

valores = []      

soma = sum(valores)

try:
    media = soma / len(valores)
    print(f"A média dos valores é: {media}")
except ZeroDivisionError:
    print("A lista está vazia. Não é possível calcular a média.")