def calcular_imc(peso, altura): [cite: 74]
    return peso / (altura ** 2) [cite: 80]

def classificar_imc(imc): [cite: 74]
    if imc < 18.5: return "Abaixo do Peso"
    elif imc < 25: return "Peso Normal"
    elif imc < 30: return "Sobrepeso"
    else: return "Obesidade"

try:
    p = float(input("Peso (kg): ")) [cite: 82]
    a = float(input("Altura (m): ")) [cite: 83]

    if p > 0 and a > 0: [cite: 77]
        resultado = calcular_imc(p, a)
        classe = classificar_imc(resultado)
        print(f"Seu IMC é {resultado:.2f} - Classificação: {classe}") [cite: 78, 84]
    else:
        print("Erro: Peso e altura devem ser positivos.")
except ValueError:
    print("Erro: Entrada inválida.")