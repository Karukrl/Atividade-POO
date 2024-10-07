salario = 1000
aumento = 1.5 / 100

for ano in range(1996, 2026):
    salario += salario * aumento
    aumento *= 2  # O aumento dobra a cada ano

print("O salário em 2025 será de R$", salario)
