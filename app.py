aparelho=input("Digite o nome do aparelho:")
potencia=float(input("Digite a potência em watts:"))
horas_dia=float(input("Digite as horas:")) 
consumo_mensal=(potencia*horas_dia*30)/1000
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal} kWh/mês")
