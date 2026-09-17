#Autor: Anderson Roberto Martins - ID: CV3132765
#Instituição: IFSP - Instituto Federal de São Paulo
#Atividade: Exercício 2 — Validação de Senha

SENHA_CORRETA = "python123"

tentativas = 0
senha_digitada = ""

while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1

    if senha_digitada != SENHA_CORRETA:
        print("Senha incorreta! Tente novamente.\n")

print("\nAcesso permitido!")
print(f"Total de tentativas usadas: {tentativas}")