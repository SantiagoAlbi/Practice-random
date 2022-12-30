# Ejercicio 1, llenar una lista con numeros del 1 al 50 y mostrarlos.
#FORMA 1
"""
lista = []

i = 1

while i <=50:
    lista.append(i)
    i+=1

print(lista)

print("")

for i in lista:
    print(i,end="-")
"""
#FORMA 2 SOLO SIRVE CUANDO LOS ELEMENTOS SEAN NUMERICOS
"""
lista = list(range(1,51))
print(lista)

#Ejercicio2

lista = list(range(1,11))

print(lista)

valor = int(input("Ingrese un numero que desea multiplicar: "))
indice = 0
for i in lista:
    lista[indice] *= valor
    indice += 1

print(lista)

for indice,i in enumerate(lista):
    lista[indice] *= valor
    indice += 1

print(lista)

#Ejercicio 3: Pide numeros y metelos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar, Ultimo,
#mostrar numeros de menor a mayor.

lista = []

salir = False

while not salir:
    numero = int(input("Inserte un numero: "))
    if numero==0:
        salir=True
    else:
        lista.append(numero)

lista.sort()

print(f"Lista ordenada es: \n{lista}")

#EJERCICIO 4: Hcaer programa para sumar numeros pares dentro de un rango

a = int(input("Digite de donde va a comenzar a sumar: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))

suma = 0

for i in range(a,b+1):
    if i%2==0:  #si el numero es par
        suma +=i

print(f"La suma es: {suma}")


#Ejercicio 5: Hcaer un programa para calcular el factorial de un numero positivo

numero = int(input("Digite un numero: "))

while numero<0:  #mientras el numero sea negativo
    print("Erros: El numero debe ser positivo")
    numero = int(input("Digite nuevamente un numero: "))

#Calcular el factorial

factorial = 1
for i in range(1,numero+1):
        factorial *= i

print(f"El factorial del {numero} es: {factorial}")
"""
#Ejercicio 6:Hacer un programa que pida numero por teclado y giarde en una lista su tabla de multiplicar
# hasta el 10. Ejemplo: si digita el 5 tendre: 1,10,15,20, hast 50
"""
numero = int(input("Ingrese un numero: "))

lista = []

for i in range(1,11):
    lista.append(i*numero)

print(f"Tabla de multiplicar:\n {lista}")
"""

#Ejercicio 7: Realizar un juego para adivinar numero, para ello generar numero aleatorio entre 0-100,luego ir pidiendo
# numeros indicando "es mayor o "es menor" segun sea con respecto a N. El proceso termina cuando usuario acierta y motrar
# numero de intentos.
"""
import random

aleatorio = random.randint(0,100)

print("Adivina el numero")
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador +=1
    if numero>aleatorio:
        print("\tNo es el numero, prueba un numero menor")
    elif numero<aleatorio:
        print("\tNo es el numero, prueba un numero meayor")
    else:
        print(f"\t Felicitaciones acabas de adivinar el numero {aleatorio}")
        break

print(f"Numero de intentos: {contador}")

"""
#EJercicio 8: Hcaer programa que simule cajero automatico con saldo disponible de 1000 y tendra las siguientes op:
# 1Ingresar dinero en la cuenta, 2, Retirar dinero.

#Simular menu de cajero automatico a retirar dinero

saldo = 1000

while True:
    print("\t.:MENU")
    print("1. Ingresar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = int(input("Ingrese opcion de menu: "))
    print()

    if opcion ==1:
        extra = float(input("Cuanto dinero desea ingresar: "))
        saldo += extra
        print(f"Dinero en la cuenta: ${saldo}")
    elif opcion ==2:
        retirar = float(input("Cuanto dinero desea retirar: "))
        if retirar>saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
        print(f"Dinero en la cuenta: ${saldo}")
    elif opcion == 3:
        print(f"Su saldo es de: ${saldo}")
    elif opcion == 4:
        print("Usted esta saliendo del sistema")
        break
    else:
        print("Opcion incorrecta, vuelva a intentarlo")

print()

