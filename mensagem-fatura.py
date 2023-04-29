cliente = input("Digite o nome do cliente: ")
diaVencimento = input("Digite o dia de vencimento: ")
mêsVencimento = input("Digite o mês de vencimento: ")
valorFatura = input("Digite o valor da fatura: ")

print("Olá,", cliente)
print("A sua fatua com vencimento em {} de {} no valor de R$ {} está fechada.".format(diaVencimento, mêsVencimento, valorFatura))
