cantidad = int(input("Cantidad: "))
lista_numeros = []

for i in range(cantidad):
    num = int(input())
    lista_numeros.append(num)

buscado = int(input("Número a buscar: "))

posicion = -1
for i in range(len(lista_numeros)):
    if lista_numeros[i] == buscado:
        posicion = i
        break 

if posicion != -1:
    print(f"El {buscado} está en la posición {posicion}")
else:
    print(f"El {buscado} no está en la lista")