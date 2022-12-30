#Como detectar si ambos numeros son pares

num1 = int(input("Ingrese un numero: "))

num2 = int(input("Ingrese un otro numero: "))

if num1%2 ==0 and num2 % 2 ==0:
    print(f"Ambos son pares {num1} y {num2}")
elif num1%2==0 and num2%2!=0:
    print(f"Primer numero {num1} es par el segundo {num2} no lo es")
elif num1%2!=0 and num2%2==0:
    print(f"Primer numero {num1} no es par el segundo {num2} si lo es")
else:
    print("Ningun numero es par")