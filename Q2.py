pares = 0
impares = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

#Aqui, eu peço 10 números ao usuário e verifico, um por um, se o número é par ou ímpar. No final, mostro a quantidade de números pares e ímpares.
