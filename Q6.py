salario = 1000
aumento = 1.5 / 100

for ano in range(1996, 2026):
    salario += salario * aumento
    aumento *= 2  # O aumento dobra a cada ano

print("O salário em 2025 será de R$", salario)
#Esse código calcula o salário de um funcionário desde 1995, onde ele ganhava R$ 1.000,00. A cada ano, o salário aumenta. No primeiro ano, o aumento é de 1,5%, e depois o aumento dobra a cada ano.
