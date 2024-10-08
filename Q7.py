divida = float(input("Digite o valor da dívida: "))

print("|Dívida   | Juros |Parcelas | Valor da Parcela|")
print(f"R$ {divida:.2f} | 0%   | 1       | R$ {divida:.2f}")

for parcelas, juros in [(3, 10), (6, 15), (9, 20), (12, 25)]:
    valor_com_juros = divida + (divida * juros / 100)
    valor_parcela = valor_com_juros / parcelas
    print(f"R$ {valor_com_juros:.2f} | {juros}%  | {parcelas}       | R$ {valor_parcela:.2f}")

#Aqui, o programa cria uma tabela para mostrar quanto a pessoa vai pagar de dívida dependendo de quantas parcelas ela escolher. Ele calcula os juros de acordo com a quantidade de parcelas.
