numero = int(input("Digite um número de 1 a 10 para ver sua tabuada: "))

print("Tabuada de", numero)
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
