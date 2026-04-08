# EXERCICIO 1

# Crie uma lista chamada países com alguns nomes de países dentro dela. Em seguida:
# - Adicione um novo país ao fim da lista
# - Adicione um novo país logo antes da posição 1
# - Remova um pais pelo nome
# - Remova um país pelo índice
# - Mostre o total de países na lista


paises = ["Brasil", "Argentina", "Chile"]
print("Lista Original")
print(paises)

paises.append("NovaYork")

print(f"Após Adicionar NY")
print(paises)

paises.insert(1, "Uruguai")

print(f"Após Adicionar Uruguai")
print(paises)

paises.remove("NovaYork")
print("Após a remoção de NY")
print(paises)

paises.pop(2)

print("Após remoção da Argentina")
print(paises)

print("Tamanho Atual da lista de Países")
print(len(paises))


# EXERCICIO 2

# CRIE UM DICIONARIO QUE ARMAZENE AS INORMAÇÕES DE UM CARRO, INFORMAÇÕES ESSAS QUE SERÃO A MARCA, MODELO E ANO. EM SEGUIDA EXIBA UMA FRASE APRESENTANDO AS INFORMAÇÕES DO CARRO, NO SEGUINTE FORMATO:

# O carro é um  MARCA MODELO do ano ANO

carro = {
    "Marca": "Toyota",
    "Modelo": "Yaris",
    "Ano": 2026
}

print(f"O carro é um {carro['Marca']} {carro['Modelo']} do ano {carro['Ano']}")

# EXERCICIO 3

# CRIE UMA LISTA COM NÚMEROS REPETIDOS, E ATRAVÉS DA CONVERSÃO DESTA PARA UM CONJUNTO, ELIMINE OS VALORES DUPLICADOS


lista = [1,4,3,1,6,5,3]

print(f"Tipo da lista: {type(lista)}")
print(lista)

conjunto_convertido = set(lista)


print(f"Tipo de conjunto convetido {type(conjunto_convertido)}")
print(conjunto_convertido)


lista_convertida = list(conjunto_convertido)
print(f"Tipo da lista convertida {type(lista_convertida)}")
print(lista_convertida)