# Semana 5 — Exercício de aula 3
# Enunciado: Peça um número e use for com range() para imprimir a tabuada
# desse número, de 1 a 10.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Saída esperada (exemplo, digitando 7):
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
