# python
Atividades em python

# Tipos básicos
nome = "Python"          # String
idade = 30               # Inteiro
altura = 1.75            # Float
estudando = True         # Booleano
frutas = ["Maçã", "Banana", "Uva"] 
aluno = {"nome": "Lucas", "nota": 8.5}

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudando: {estudando}")
print(f"Lista de frutas: {frutas}")
print(f"Dicionário do aluno: {aluno}")

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("Erro: O nome deve ter mais de 3 caracteres.")

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"Olá {nome}, o número {numero} é PAR.")
else:
    print(f"Olá {nome}, o número {numero} é ÍMPAR.")

    import math

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

print(f"Soma: {n1 + n2}")
print(f"Subtração: {n1 - n2}")
print(f"Multiplicação: {n1 * n2}")
print(f"Divisão: {n1 / n2}")
print(f"Raiz quadrada de {n1}: {math.sqrt(n1)}")
print(f"Logaritmo de {n1} na base {n2}: {math.log(n1, n2)}")

print("1- Mouse (R$50) | 2- Teclado (R$100) | 3- Monitor (R$800)")
opcao = int(input("Escolha o produto: "))
qtd = int(input("Quantidade: "))

precos = {1: 50, 2: 100, 3: 800}
total = precos[opcao] * qtd

# Desconto se comprar 5 ou mais itens
if qtd >= 5:
    total *= 0.90 # 10% de desconto

print("Frete: 1- Correio (R$20) | 2- Transportadora (R$40) | 3- Motoboy (R$15)")
tipo_frete = int(input("Escolha o frete: "))
fretes = {1: 20, 2: 40, 3: 15}

print(f"Total a pagar: R$ {total + fretes[tipo_frete]}")

print("1- Mouse (R$50) | 2- Teclado (R$100) | 3- Monitor (R$800)")
opcao = int(input("Escolha o produto: "))
qtd = int(input("Quantidade: "))

precos = {1: 50, 2: 100, 3: 800}
total = precos[opcao] * qtd

# Desconto se comprar 5 ou mais itens
if qtd >= 5:
    total *= 0.90 # 10% de desconto

print("Frete: 1- Correio (R$20) | 2- Transportadora (R$40) | 3- Motoboy (R$15)")
tipo_frete = int(input("Escolha o frete: "))
fretes = {1: 20, 2: 40, 3: 15}

print(f"Total a pagar: R$ {total + fretes[tipo_frete]}")


import random

print("Dificuldade: 1-Fácil (1-10) | 2-Médio (1-50) | 3-Difícil (1-100)")
nivel = int(input("Escolha: "))
limite = 10 if nivel == 1 else 50 if nivel == 2 else 100

segredo = random.randint(1, limite)
palpite = 0

while palpite != segredo:
    palpite = int(input(f"Chute um número entre 1 e {limite}: "))
    if palpite < segredo:
        print("Mais alto!")
    elif palpite > segredo:
        print("Mais baixo!")

print("Parabéns! Você acertou.")


t1 = float(input("Nota Trabalho 1: "))
p1 = float(input("Nota Prova 1: "))
media_trimestre = (t1 + p1) / 2

if media_trimestre >= 7:
    situacao = "Aprovado"
elif media_trimestre >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media_trimestre} - Situação: {situacao}")


altura = float(input("Sua altura em cm: "))
peso = float(input("Seu peso em kg: "))
sexo = input("Sexo (M/F): ").upper()

if sexo == "M":
    ideal = (altura - 100) - (altura - 150) / 4
else:
    ideal = (altura - 100) - (altura - 150) / 2

imc = peso / ((altura/100) ** 2)

print(f"Seu peso ideal é: {ideal:.2f}kg")
print(f"Seu IMC é: {imc:.2f}")


valor_compra = float(input("Valor total da compra: R$ "))
print("1- À vista (dinheiro/pix) | 2- Parcelado")
forma = int(input("Escolha: "))

if forma == 1:
    print(f"Total: R$ {valor_compra}")
else:
    parcelas = int(input("Quantas parcelas? "))
    # Adicionando 5% de juros se parcelar
    total_com_juros = valor_compra * 1.05
    valor_parcela = total_com_juros / parcelas
    print(f"Total com juros: R$ {total_com_juros:.2f} em {parcelas}x de R$ {valor_parcela:.2f}")

