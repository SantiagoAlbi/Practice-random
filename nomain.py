#Ejercicio 4 Hacer programa para ingresar radio de un circulo y se reporte area y ong de su circunferencia

import math

radio = float(input("Ingrese el radio "))
area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El area es {area}")
print(f"La longitud es {longitud}")

print(f"El area es {area:.3f}")

#Ejercicio 4 descuento 15% y el usuario quiere saber cuanto debe pagar.

precio = float(input("Precio de producto: "))
descuento = precio * 0.15
precio_final = precio - descuento

print(f"El valor a pagar es {precio_final}")