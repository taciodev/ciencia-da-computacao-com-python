numero_int = input("Digite um número inteiro: ")

if len(numero_int) >= 2:
    print("O dígito das dezenas é", numero_int[-2])
else:
    print("O digito das dezenas é", 0)
