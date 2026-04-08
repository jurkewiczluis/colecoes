dicionario = {
    "nome": "Luis",
    "estado": "São Paulo",
    "altura": 1.73
}

print(f"Tipo do meu dicionario: {type(dicionario)}")

print("Dicionario antes da modificação")
print(dicionario)

dicionario["nome"] = "Dev Luis"
dicionario["Linguagem"] = "Python"

print("Dicionario Depois da modificação")
print(dicionario["nome"])
print(dicionario["estado"])