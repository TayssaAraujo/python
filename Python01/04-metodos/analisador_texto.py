texto_original = input("Digite o texto: ") [cite: 107]

# Normalização [cite: 101, 120]
texto_limpo = texto_original.lower()
for char in ",.;:!?":
    texto_limpo = texto_limpo.replace(char, "")

palavras = texto_limpo.split() [cite: 105]

print(f"Palavras: {len(palavras)}") [cite: 108]
print(f"Caracteres (com espaços): {len(texto_original)}") [cite: 109]
print(f"Caracteres (sem espaços): {len(texto_original.replace(' ', ''))}") [cite: 110]

# Top 3 (Lógica simples) [cite: 97]
contagem = {p: palavras.count(p) for p in set(palavras)}
top_3 = sorted(contagem.items(), key=lambda x: x[1], reverse=True)[:3]
print(f"Top 3: {', '.join([f'{k}({v})' for k, v in top_3])}") [cite: 111]

inicio = input("Começa com qual palavra? ").lower()
print("Sim" if texto_limpo.startswith(inicio) else "Não") [cite: 112, 113]

fim = input("Termina com qual palavra? ").lower()
print("Sim" if texto_limpo.endswith(fim) else "Não") [cite: 114, 115]

print(f"Texto normalizado: {' '.join(palavras)}") [cite: 116]