# Variables
sueldo_base = 0
descuento_legal = 0.20

# Entrada 

sueldo_base = int(input("Ingrese su sueldo base: "))
descuento_legal = float(input("Ingrese decuento legal (0.20): "))

# Calculo

sueldo_liquido = sueldo_base - (sueldo_base * descuento_legal) 

# Salida 

print("Total sueldo liquido: $", sueldo_liquido),