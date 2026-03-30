
# Variables

total_dinero = 0
inversion_bono = ""
n_meses = 0
tasa_bono = 0.05
tasa_deposito = 0.10

# Entrada

total_dinero = float(input("Ingrese cantidad de dinero: "))
inversion_bono = float(input("¿Cuánto dinero invertirá en bonos hipotecarios?: "))
n_meses = int(input("Ingrese el numero de meses: "))

# Calculo

inversion_deposito = total_dinero - inversion_bono 

ganancia_bonos = inversion_bono * tasa_bono * n_meses
ganancia_deposito = inversion_deposito * tasa_deposito * n_meses

ganancia_total = ganancia_bonos + ganancia_deposito

# Salida
print("La ganancia total despues de", n_meses, "meses es de: $", ganancia_total)