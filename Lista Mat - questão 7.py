def euclides(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

MDC = euclides(numero_1, numero_2)
print("O máximo divisor comum entre", numero_1, "e", numero_2, "é", MDC)
