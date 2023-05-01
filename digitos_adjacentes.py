numero = input("Digite um número inteiro: ")

contador = 1
adjacenteIgual = False

while contador < len(numero):
    if numero[contador - 1] == numero[contador]:
        adjacenteIgual = True

    contador += 1

if adjacenteIgual:
    print("sim")
else:
    print("não")
