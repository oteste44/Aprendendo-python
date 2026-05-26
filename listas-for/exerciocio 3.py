listaPrincipal = []
impares = []
pares = []


for i in range(10):
 numero = int(input(f"Digite umnúmero: "))
 if numero % 2 == 0:
    impares.append(numero)

 else:
    pares.append(numero)

print('-----------------------------------')
print()
print(impares)
print(pares)