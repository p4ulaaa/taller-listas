numeros = []

print("Ingrese números enteros (escriba 99999 para terminar):")
while True:
    num = int(input())
    if num == 99999:
        break
    numeros.append(num)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Pares: {pares} (total {len(pares)})")
print(f"Impares: {impares} (total {len(impares)})")