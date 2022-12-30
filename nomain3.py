#Hacer programa que pida 3 numeros y determine cual es el mayor
"""
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un segundo numero: "))
num3 = float(input("Ingrese un tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El primer numero {num1} es el mayor")
elif num2 >= num1 and num2 >= num3:
    print(f"El segundo numero {num2} es el mayor")
else:
    print(f"El tercer numero {num3} es el mayor")

#Buscar si hay vocales en palabras

letra = input("digite un caracter: ").lower()

if letra == "a" or letra == "b" or letra == "c" or letra == "d" or letra == "e":
    print("Es una vocal")
else:
    print("No es una vocal")


#Hacer calculadora y que con solo un caracter el usuario indique que operacion realizar.

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))

operacion = input("Digite una operacion: ").upper()

if operacion == "S":
    suma = num1+num2
    print(f"El resultado es: {suma}")
elif operacion == "R":
    resta = num1-num2
    print(f"El resultado es: {resta}")
elif operacion == "M":
    multiplicacion = num1*num2
    print(f"El resultado es: {multiplicacion}")
elif operacion == "D":
    div = num1/num2
    print(f"El resultado es: {div}")
else:
    print("Orden no posuble, se equivoco")
"""
#Simular menu de cajero automatico a retirar dinero

saldo = 1000
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
    print(f"Dinero en la cuenta: {saldo}")
elif opcion ==2:
    retirar = float(input("Cuanto dinero desea retirar: "))
    if retirar>saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retirar
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Su saldo es de: {saldo}")
elif opcion == 4:
    print("Usted esta saliendo del sistema")
else:
    print("Opcion incorrecta, vuelva a intentarlo")
