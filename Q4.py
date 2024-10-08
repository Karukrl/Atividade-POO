populacao_A = 80000
populacao_B = 200000
anos = 0

while populacao_A < populacao_B:
    populacao_A = populacao_A + (populacao_A * 0.03)
    populacao_B = populacao_B + (populacao_B * 0.015)
    anos += 1

print("Serão necessários", anos, "anos para a população de A ultrapassar ou igualar a de B.")
#Esse código calcula quanto tempo vai demorar para a população do país A, que está crescendo mais rápido, ultrapassar a população do país B. Ele faz isso simulando o crescimento de ambos ano a ano.
