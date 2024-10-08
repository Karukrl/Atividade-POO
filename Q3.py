#Aqui, o programa recebe um número e testa se ele é primo. Ele faz isso verificando se o número é divisível apenas por 1 e por ele mesmo. Se encontrar algum divisor, ele já sabe que não é primo.


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
