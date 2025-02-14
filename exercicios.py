"""
Exercícios
1 - Imprima a frase: Python na Escola de Programação da Alura.

2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores 
armazenados em variáveis.

3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado
em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

"""

# Exercício 1
print("Python na Escola de Programação da Alura")

# Exercício 2
nome = "McCloud"
idade = 457

print(f"Meu nome é {nome} e tenho {idade} anos")

# Exercício 3
print("A\nL\nU\nR\nA")
print("")

for x in "ALURA":
    print(x)

# Exercício 4
pi = 3.14159265359
pi_arredondado = round(pi, 2)
print(f"O valor arredondado de pi é: {pi_arredondado}")

# Exemplo com sep:
print("P", "Y", "T", "H", "O", "N", sep="\n")


