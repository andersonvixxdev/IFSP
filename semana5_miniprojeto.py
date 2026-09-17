
#Autor: Anderson Roberto Martins - ID: CV3132765
#Instituição: IFSP - Instituto Federal de São Paulo
#Atividade: Semana 5 - Mini Projeto - Cálculo de Média e Aprovados

qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))

soma_notas = 0.0
aprovados = 0

for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    soma_notas += nota

    if nota >= 6:
        aprovados += 1

if qtd_alunos > 0:
    media = soma_notas / qtd_alunos
    print("\n--- Resultado da Turma ---")
    print(f"Média da turma: {media:.2f}")
    print(f"Total de aprovados: {aprovados}")
else:
    print("Nenhum aluno informado.")