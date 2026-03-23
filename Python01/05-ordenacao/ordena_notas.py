notas = []
n = int(input("Quantas notas? ")) [cite: 137]

while len(notas) < n:
    try:
        nota = float(input(f"Nota {len(notas)+1}: "))
        if 0 <= nota <= 10: [cite: 134]
            notas.append(nota)
        else:
            print("Nota inválida! Digite entre 0 e 10.")
    except ValueError:
        print("Digite um número válido.")

notas.sort() [cite: 135]
media = sum(notas) / n

# Mediana [cite: 135, 149, 150]
if n % 2 != 0:
    mediana = notas[n // 2]
else:
    mediana = (notas[n // 2 - 1] + notas[n // 2]) / 2

print(f"Ordenado (crescente): {notas}") [cite: 143]
print(f"Maior: {max(notas)} | Menor: {min(notas)} | Média: {media:.1f} | Mediana: {mediana:.1f}") [cite: 144]

if input("Exibir em ordem decrescente? (s/n): ").lower() == 's': [cite: 145]
    print(sorted(notas, reverse=True)) [cite: 146]