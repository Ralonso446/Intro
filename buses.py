# Variables
bus_uno = "0"
bus_dos = "0"
total_pasajeros = "0"
valor_pasaje = "0"
recaudacion_total = "0"
ciudad = ""

# Entrada
ciudad = input("Destino a: ")

bus_uno = int(input("Pasajeros que se fueron en el bus uno: "))
bus_dos = int(input("Pasajeros que se fueron en el bus dos: "))
valor_pasaje = int(input("Ing. valor del pasaje: "))

total_pasajeros = bus_uno + bus_dos
recaudacion_total = total_pasajeros * valor_pasaje 

print("Total recaudado: recaudacion_total")