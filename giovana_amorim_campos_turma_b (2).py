# -*- coding: utf-8 -*-
"""Giovana Amorim Campos - Turma B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1farxPZhYCUgUh4QSP4rDVb_gVr-Un0A9
"""

numero_inteiro_1 = 25
print(numero_inteiro_1)

texto_1 = "Oi Python!"
print(texto_1)
print(type(texto_1))

numero_inteiro_2 = 5
print(numero_inteiro_2)
print(type(numero_inteiro_2))

numero_decimal_1 = 25.5
print(type(numero_decimal_1))

numero_inteiro_1 = 25
numero_inteiro_2 = 5
div = numero_inteiro_1 / numero_inteiro_2
print(div)

pessoa_1 = "Gabriel"
numero_1 = 5
print(numero_1)
print(pessoa_1)
pessoa_1 == "Gabriel"
pessoa_1 == "Felipe"

pessoa_1 = "Gabriel"
pessoa_1 == "Gabriel"

numero_1 = 5
numero_1 == 5

nota = 7
if nota > 9:
  print("Parabéns!")
elif nota >= 7:
  print("Você passou!")
elif nota > 5 and nota < 7:
  print("Você deve fazer a recuperação!")
else:
  print("Você reprovou!")

numero = -5
if numero == 0:
  print("O número é zero")
else:
  if numero > 0:
    print("O número é positivo")
  else:
    print("O número é negativo")

numero = 7
if numero > 0:
  if numero % 2 == 0 and numero < 10:
    print("O número é par, positivo e menor que 10")
  else:
    print("O número não atende aos critérios!")