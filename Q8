gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

maior_acerto = 0
menor_acerto = 10
total_alunos = 0
soma_notas = 0

continuar = 's'

while continuar == 's':
    acertos = 0
    for i in range(10):
        resposta = input(f"Digite a resposta da questão {i+1}: ").upper()
        if resposta == gabarito[i]:
            acertos += 1

    print("Você acertou", acertos, "questões.")

    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos
    
    soma_notas += acertos
    total_alunos += 1

    continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").lower()

media_notas = soma_notas / total_alunos

print("Maior acerto:", maior_acerto)
print("Menor acerto:", menor_acerto)
print("Total de alunos:", total_alunos)
print("Média da turma:", media_notas)
