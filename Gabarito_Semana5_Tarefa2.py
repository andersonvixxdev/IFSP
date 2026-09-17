# Semana 5 — Tarefa de casa, questão 2 (nível iniciante)
# Enunciado: Simule uma verificação de senha: defina uma senha fixa no
# código e use um while para pedir a senha repetidamente até o usuário
# acertar, contando e exibindo no final quantas tentativas foram usadas.

senha_correta = "python123"
tentativas = 0

senha_digitada = input("Digite a senha: ")
tentativas += 1

while senha_digitada != senha_correta:
    senha_digitada = input("Senha incorreta. Tente novamente: ")
    tentativas += 1

print(f"Senha correta! Você usou {tentativas} tentativa(s).")

# Saída esperada (exemplo, acertando na 3ª tentativa):
# Senha correta! Você usou 3 tentativa(s).
