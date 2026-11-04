N = int(input("¿Cuántas letras se van a ingresar? "))
letras = []

for i in range(N):
    letra = input(f"Letra {i+1}: ").lower()
    letras.append(letra)

conteo_a = letras.count('a')
conteo_e = letras.count('e')
conteo_i = letras.count('i')
conteo_o = letras.count('o')
conteo_u = letras.count('u')

if conteo_a > 0: print(f"a: {conteo_a}")
if conteo_e > 0: print(f"e: {conteo_e}")
if conteo_i > 0: print(f"i: {conteo_i}")
if conteo_o > 0: print(f"o: {conteo_o}")
if conteo_u > 0: print(f"u: {conteo_u}")