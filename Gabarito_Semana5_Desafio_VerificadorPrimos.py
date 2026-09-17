# Semana 5 — Tarefa de casa, desafio intermediário
# Enunciado: Construa um verificador de números primos: peça ao usuário
# um número inteiro maior que 1. Usando um laço for, teste se algum
# número entre 2 e o número menos 1 divide ele exatamente (resto zero).
# Um número primo é aquele que não é divisível por nenhum número além de
# 1 e ele mesmo. Ao final, informe se o número é primo ou não, e quantos
# divisores diferentes de 1 e dele mesmo foram encontrados.

numero = int(input("Digite um número inteiro maior que 1: "))
divisores = 0

for i in range(2, numero):
    if numero % i == 0:
        divisores += 1

if divisores == 0:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo. Foram encontrados {divisores} divisor(es) além de 1 e ele mesmo.")

# Saída esperada (exemplo, digitando 7): 7 é primo.
# Saída esperada (exemplo, digitando 9): 9 não é primo. Foram encontrados 1 divisor(es) além de 1 e ele mesmo.
