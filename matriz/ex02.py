def menu():
    while True:
        print("""
========================
   E-COMMERCE SYSTEM
========================
[1] Visualizar estoque
[2] Adicionar ao carrinho
[3] Visualizar carrinho
[4] Finalizar compra
[0] Sair
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            mostrar_estoque()

        elif opcao == "2":
            adicionar_ao_carrinho()

        elif opcao == "3":
            visualizar_carrinho()

        elif opcao == "4":
            finalizar_compra()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


estoque = {
    1: {"nome": "Teclado", "preco": 150.00, "quantidade": 15},
    2: {"nome": "Mouse", "preco": 80.00, "quantidade": 22},
    3: {"nome": "Monitor", "preco": 900.00, "quantidade": 8}
}

carrinho = []



def mostrar_estoque():
    print("\n--- ESTOQUE ---")
    print(f"{'ID':<5}{'Produto':<15}{'Preço':<12}{'Qtd'}")

    for id_produto, dados in estoque.items():
        print(f"{id_produto:<5}{dados['nome']:<15}R$ {dados['preco']:<10.2f}{dados['quantidade']}")



def adicionar_ao_carrinho():
    mostrar_estoque()

    try:
        id_produto = int(input("\nDigite o ID do produto: "))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Digite apenas números.")
        return

    if id_produto not in estoque:
        print("Produto não encontrado.")
        return

    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    produto = estoque[id_produto]

    if quantidade > produto["quantidade"]:
        print("Estoque insuficiente.")
        return


    produto["quantidade"] -= quantidade


    carrinho.append({
        "id": id_produto,
        "nome": produto["nome"],
        "preco": produto["preco"],
        "quantidade": quantidade
    })

    print(f"{produto['nome']} adicionado ao carrinho!")


def visualizar_carrinho():
    if not carrinho:
        print("\nCarrinho vazio.")
        return

    print("\n--- CARRINHO ---")
    total = 0

    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal

        print(f"{item['nome']} | {item['quantidade']}x R$ {item['preco']:.2f} = R$ {subtotal:.2f}")

    print(f"\nSubtotal: R$ {total:.2f}")



def finalizar_compra():
    if not carrinho:
        print("\nCarrinho vazio.")
        return

    subtotal = sum(item["preco"] * item["quantidade"] for item in carrinho)

    cupom = input("Digite o cupom (ou ENTER para nenhum): ").upper()

    desconto = 0

    if cupom == "DEV10":
        desconto = subtotal * 0.10

    elif cupom == "DEV20" and subtotal > 500:
        desconto = subtotal * 0.20

    total = subtotal - desconto

    print("\n--- RESUMO DA COMPRA ---")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total: R$ {total:.2f}")

    confirmar = input("\nConfirmar pagamento? (s/n): ").lower()

    if confirmar == "s":
        carrinho.clear()
        print("Compra finalizada com sucesso!")

    else:

        for item in carrinho:
            estoque[item["id"]]["quantidade"] += item["quantidade"]

        carrinho.clear()
        print("Compra cancelada. Estoque restaurado.")






menu()
