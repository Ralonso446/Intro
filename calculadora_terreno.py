# Variables

ancho = "0"
largo = "0"
terreno = "0"
valor_total = "0"
valor = "0"

print("---------$ Calculador de terreno $---------")
# Entrada

ancho = int(input("¿Cuál es el ancho de su terreno?: "))
largo = int(input("¿Cual es el largo de su terreno?: "))
valor = int(input("Ingrese el valor del metro cuadrado: "))

terreno = largo * ancho 
valor_total = ancho * largo * valor

# Salida
print(f"Valor del terreno es: {valor_total}")