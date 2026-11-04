N = int(input("Cantidad de temperaturas: "))
temperaturas = []

for i in range(N):
    temp = float(input())
    temperaturas.append(temp)

if N > 0:
    media = sum(temperaturas) / N
else:
    media = 0.0

superiores = []
for t in temperaturas:
    if t >= media:
        superiores.append(t)

print(f"Temperatura media: {media}")
print(f"Temperaturas >= media: {superiores}")
print(f"Total: {len(superiores)}")