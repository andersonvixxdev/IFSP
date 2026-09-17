# Semana 5 — Tarefa de casa, questão 1 (nível iniciante)
# Enunciado: Peça um número inteiro positivo e use um laço para calcular
# e imprimir o fatorial desse número (ex.: fatorial de 5 é 5×4×3×2×1 = 120).

numero = int(input("Digite um número inteiro positivo: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")

# Saída esperada (exemplo, digitando 5):
# O fatorial de 5 é 120
