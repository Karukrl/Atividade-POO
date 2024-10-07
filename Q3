#Questão 3 (1.5 pontos): Faça um programa que peça um número inteiro e determine se ele é ou não#
#um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.#

numero = int(input("Digite um número: "))

if numero > 1:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(numero, "é primo")
    else:
        print(numero, "não é primo")
else:
    print(numero, "não é primo")
