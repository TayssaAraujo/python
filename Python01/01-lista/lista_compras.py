'''lista de compras'''

lista_compras = []

while True:
    print("\n--- MENU ---")
    print("1-Adicionar, 2-Remover, 3-Listar, 4-Buscar, 0-Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        item = input("Digite o item: ").strip().lower() # Normalização para evitar duplicatas [cite: 22, 43]
        if item not in lista_compras:
            lista_compras.append(item)
            print("Item adicionado!")
        else:
            print("Erro: Este item já está na lista.") [cite: 22]

    elif opcao == '2':
        item = input("Remover qual item? ").strip().lower()
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido.") [cite: 39]
        else:
            print("Erro: Item não encontrado.") [cite: 23]

    elif opcao == '3':
        print("\nLista de Compras:")
        for i, item in enumerate(lista_compras, 1): # Lista numerada [cite: 24]
            print(f"{i}) {item}")

    elif opcao == '4':
        busca = input("Buscar por: ").strip().lower()
        if busca in lista_compras:
            # Encontra todas as posições caso haja duplicatas manuais [cite: 25, 43]
            posicoes = [i + 1 for i, x in enumerate(lista_compras) if x == busca]
            print(f"Encontrado nas posições: {', '.join(map(str, posicoes))}")
        else:
            print("Item não encontrado.")

    elif opcao == '0':
        print("Encerrando...") [cite: 41]
        break