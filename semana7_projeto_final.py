# Autor: Anderson Roberto Martins - ID: CV3132765
# Instituição: IFSP - Instituto Federal de São Paulo
# Projeto Final: Caixa Registradora Simples

total_compra = 0.0
quantidade_itens = 0

while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")

    if nome_produto.lower() == "sair":
        break

    preco = float(input(f"Digite o preço de {nome_produto}: R$ "))

    total_compra += preco
    quantidade_itens += 1

print("-" * 30)

if quantidade_itens == 0:
    print("Nenhum item foi adicionado.")
else:
    print(f"Itens comprados: {quantidade_itens}")
    print(f"Total sem desconto: R$ {total_compra:.2f}")

    total_a_pagar = total_compra

    if total_compra > 100.0:
        desconto = total_compra * 0.10
        total_a_pagar = total_compra - desconto
        print("Desconto de 10% aplicado (compra acima de R$100)!")

    print(f"Total a pagar: R$ {total_a_pagar:.2f}")
    print("Obrigado pela compra!")