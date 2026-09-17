#Autor: Anderson Roberto Martins - ID: CV3132765
#Instituição: IFSP - Instituto Federal de São Paulo
#Atividade: Exercício 1 — Cálculo do Fatorial


num = int(input("Digite um número inteiro positivo: "))

fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é: {fatorial}")