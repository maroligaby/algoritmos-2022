# -*- coding: utf-8 -*-
"""lista 9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wTgtEyHuEfo2j_LIvbOwEJWDWkPzEXfI
"""

#questão 1
def primo(n):
    for val in range(2,n):
        if n % val == 0:
            return False
    return True

numeros = [2,6,8,3,9,13,17,16,21]
primos = []

for numero in numeros:
  if (primo(numero) == True):
    primos.append(numero)

for primo in primos:
  print("O número ", primo, " é primo")
  posicao = numeros.index(primo)
  print("Ele está na posição ", posicao)

#questão 2
salario = 545
porcentagem = 5
objetos = ["caneta","lápis","borracha","apontador","folha a4","corretivo","grampeador","pasta","lapiseira","grafite"]
valor_unitario = []
quantidade_vendida = []

for objeto in objetos:
  print("ITEM: ", objeto)
  vlr = float(input("Qual o valor unitário?"))
  valor_unitario.append(vlr)
  qtd = int(input("Qtos foram vendidos"))
  quantidade_vendida.append(qtd)

print("RElatório")
print("Objeto | Qtd | Vlr Unitário | Valor Total ")
for i in (range(0,len(objetos))):
  print(objetos[i], " | ", valor_unitario[i], " | ", quantidade_vendida[i], " | ", quantidade_vendida[i] * valor_unitario[i])