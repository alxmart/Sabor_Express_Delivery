"""
Como já vimos, programação é prática! 
Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e reforçar ainda mais seu aprendizado 
e o conteúdo da vez são dicionarios. Bora praticar?

Exercícios
"""
#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {
    "nome": "McCloud",
    "idade": 456,
    "cidade": "São Paulo"
}

print(pessoa)

#2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoa["idade"] = 457

# Adicione um campo de profissão para essa pessoa;
pessoa["profissao"] = "Warrior"

# Remova um item do dicionário.
del pessoa["cidade"]

print(pessoa)

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

print(quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
cidades = {
    "city1": "London",
    "city2": "São Paulo",
    "city3": "New York"
}

key = "city4"

if key in cidades:
    print(f"A chave '{key}' existe no dicionário.")
else:    
    print(f"A chave '{key}' não existe no dicionário.")  

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos. Python"

contagem_palavras = {}

palavras = frase.split()
print(palavras)

for word in palavras:
    contagem_palavras[word] = contagem_palavras.get(word, 0) + 1

print(contagem_palavras)