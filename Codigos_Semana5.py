# =============================================================
# CÓDIGOS DA AULA — SEMANA 5
# Estruturas de Repetição em Python
# Introdução à Programação em Python — IFSP Câmpus Capivari
# =============================================================
# Este arquivo reúne todos os códigos digitados em aula hoje,
# organizados por seção. Pode rodar o arquivo inteiro de uma vez
# (a última seção vai pedir dados pelo teclado) ou copiar só o
# trecho que quiser testar separadamente.

# -------------------------------------------------------------
# 1) O QUE É UM LAÇO
# -------------------------------------------------------------
contador = 1
while contador <= 5:
    print(contador)
    contador += 1


# -------------------------------------------------------------
# 2) while — CONTADORES E ACUMULADORES
# -------------------------------------------------------------
soma = 0
numero = 1
while numero <= 10:
    soma += numero
    numero += 1
print(f"A soma de 1 a 10 é {soma}")


# -------------------------------------------------------------
# 3) for E range()
# -------------------------------------------------------------
for i in range(1, 6):
    print(f"Repetição número {i}")


# -------------------------------------------------------------
# 4) ITERANDO SOBRE STRINGS
# -------------------------------------------------------------
palavra = "python"
for letra in palavra:
    print(letra.upper())


# -------------------------------------------------------------
# 5) REPETIÇÕES ANINHADAS
# -------------------------------------------------------------
for numero in range(1, 4):
    for multiplicador in range(1, 4):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")


# -------------------------------------------------------------
# 6) MINI-PROJETO: SISTEMA DE NOTAS DA TURMA (código completo)
# -------------------------------------------------------------
qtd_alunos = int(input("Quantos alunos tem a turma? "))
soma_notas = 0
aprovados = 0

for i in range(qtd_alunos):
    nota = float(input(f"Nota do aluno {i + 1}: "))
    soma_notas += nota
    if nota >= 6:
        aprovados += 1

media_turma = soma_notas / qtd_alunos
print(f"Média da turma: {media_turma:.2f}")
print(f"Aprovados: {aprovados} de {qtd_alunos}")
