# Columbian Pesos
pesos = int(input("Enter the amount of pesos: "))
pesos_to_dollars = pesos * 0.050
# Peruvian Soles
soles = int(input("Enter the amount of soles: "))
soles_to_dollars = soles * 0.30
# Brazilian Reais
reais = int(input("Enter the amount of reais: "))
reais_to_dollars = reais * 0.25
total = pesos_to_dollars + soles_to_dollars + reais_to_dollars
print("The total amount of dollars is " + str(total))