numero = int(input("Digite um número inteiro: "))

i = 1
numerosDivisiveis = 0

while i <= numero:
    if numero % i == 0:
    	numerosDivisiveis += 1
    i += 1
    
if numerosDivisiveis == 2:
	print("primo")
else:
	print("não primo")


