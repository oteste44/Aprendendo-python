listaPrincipal = []
impares = []
pares = []


for i in range(10):
 numero = int(input(f"Digite umnúmero: "))
 if numero % 2 == 0:
    impares.append(numero)
    print('PAR')

 else:
    pares.append(numero)
    print('IMPAR')

print('-----------------------------------')
print()

print(pares)
print(impares)
