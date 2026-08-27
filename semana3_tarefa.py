
//Programa: Entrega de TAREFA - Semana 3
//Autor: Anderson Roberto Martins - ID: CV3132765
//Instituição: IFSP - Instituto Federal de São Paulo
//Atividade: Semana 2 - Exercício de Entrada e Saída de Dados


# Questão 1 - Soma, média e produto de dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
media = (numero1 + numero2) / 2
produto = numero1 * numero2

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")


# Questão 2 - Contagem de caracteres com len()
texto = input("Digite um texto: ")

quantidade_caracteres = len(texto)

print(f"Quantidade de caracteres: {quantidade_caracteres}")