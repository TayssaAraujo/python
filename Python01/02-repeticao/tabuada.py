while True:
    try:
        base = int(input("Número base: "))[cite: 57]

        while True:
            inicio = int(input("Início: "))[cite: 58]
            fim = int(input("Fim: "))[cite: 59]
            if inicio <= fim: [cite: 54]
            break
        print("Erro: O início deve ser menor ou igual ao fim!")

    for i in range(inicio, fim + 1): [cite: 66]
    print(f"{base} x {i} = {base * i}")[cite: 54]

cont = input("Calcular outra? (s/n): ").lower()[cite: 55]
if cont != 's':
    break
except ValueError:
print("Erro: Digite apenas números inteiros.")[cite: 67]