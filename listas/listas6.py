# pop(valor)

lista = [254, False, "Caneta"]
print(f"Tipo da lista {type(lista)}")

print("Lista antes do pop:")
print(lista)


tam = len(lista)
print(f"Tamanho da lista: {tam}")

lista.pop(1)

print("Lista após o pop:")
print(lista)

tam = len(lista)
print(f"Tamanho da lista: {tam}")

