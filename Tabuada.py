numero = int(input("Digite um número de 1 a 10 para ver sua tabuada: "))

print("Tabuada de", numero)
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
#Aqui, o programa pede o número da tabuada e, depois, faz a multiplicação desse número por todos os valores de 1 até 10, mostrando o resultado um por um.
