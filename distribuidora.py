# Variables
cajas = 0
mause = 0 
valor_unitario = 0
total_cancelar = 0


# Entrada

cajas = int(input("Ingrese el numero total de cajas: "))
mause = int(input("Ingrese el numero total de mause: "))
valor_unitario = int(input("Ingrese el valor total de mause: "))

total_cancelar = cajas * mause * valor_unitario

# Salida
print("Usted debe cancelar un total de: ", total_cancelar)