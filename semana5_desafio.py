
#Autor: Anderson Roberto Martins - ID: CV3132765
#Instituição: IFSP - Instituto Federal de São Paulo
#Atividade: Semana 5 - Desafio

num = int(input("Digite um número inteiro maior que 1: "))

outros_divisores = 0

for i in range(2, num):
    if num % i == 0:
        outros_divisores += 1

print("\n--- Resultado ---")
print(f"Divisores encontrados (além de 1 e ele mesmo): {outros_divisores}")

if outros_divisores == 0:
    print(f"O número {num} é PRIMO!")
else:
    print(f"O número {num} NÃO é primo.")