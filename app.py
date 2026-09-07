aparelho=input("geladeira")
potencia=float(input("digite a potência em watts:"))
horas_dia=float(input("digite as horas:"))
consumo_mensal=(potencia*horas_dia*30)/1000
print(consumo_mensal)
