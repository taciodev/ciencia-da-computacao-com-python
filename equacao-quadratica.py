import math

a = int(input("Qual o valor da constante A: "))
b = int(input("Qual o valor da constante B: "))
c = int(input("Qual o valor da constante C: "))

delta = (b ** 2) - 4 * a * c

if delta < 0: 
    print("Essa equação não possui solução real.")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    if delta >= 0:
        print("RAIZ 1=", raiz1)
    if delta > 0:
        print("RAIZ 2=", raiz2)

