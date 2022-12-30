#Bucle While
"""
import math

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrara es: {(math.sqrt(numero)):.3f}")

i = 0

while i<10:
    print("Hola Mundo")
    i += 1
"""
#BUCLE FOR funciona en todas las colecciones con diccionario es especial(muestra las claves por defecto)
"""
for i in [1,2,3,4,5]:
    print("Hola Mundo")

for i in [2,10,3,4,"Santiago"]:
    print(f"Elemento: {i}")

coleccion = [2,10,3,4,"Santiago"]
for i in coleccion:
    print(f"Elemento: {i}")
"""
"""
coleccion = {"Santiago": 38, "Maria": 26, "Alessia": 29}

for i in coleccion:
    print(i)
#Esta manera solo muestra la clave del diccionario por defecto

for i in coleccion:
    print(f"{coleccion[i]}")

#Esta manera muestra los valores de las claves

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")

#Esta manera imprime clave y valor del diccionario.

for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")

#Esta ultima manera es mas profesional para recorrer un diccionario.

#Ejemplo siguiente es sobre una cadena.

coleccion = "Santiago"

for i in coleccion:
    print(f"{i}", end=" ") #con. el "end" no hay salto de linea
"""
#FOR RANGE

for i in range(50): #crea una coleccion ficticia donde recorre si o si 50 veces dicha coleccion.
    print(i)

for i in range(5,11): #va del 5 al 10, el ultimo indice no se imprime
    print(i)

for i in range(2,21,2): #Aqui el 3er item es para indicar de cuento en cuanto va a realizar la iteracion.
    print(i)

for i in range(20,1,-2): #Va de manera inversa al anterior ejemplo
    print(i)