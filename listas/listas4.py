# INSERT -> insert(posição, valor)

lista = [5.4, 5.5, 5.6]

print(f"Tipo de lista: {type(lista)}")

print("Lista antes do insert")
print(lista)

lista.insert(2, 5.55)
print("Lista apos insert:")
print(lista)
