segundos_total = input("Por favor, digite o número de segundo que você deseja converter: ")
segundos_total = int(segundos_total)

dia = segundos_total // 86400
print("DIA:", dia)
horas = segundos_total // 3600
minutos = (segundos_total % 3600) // 60
segundos = (segundos_total % 3600) % 60

print(horas, "horas,", minutos, "minutos e", segundos, "segundos.")
