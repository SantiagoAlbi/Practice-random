# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

#Ejercicio 1

a = float(input("a -> "))
b = float(input("b -> "))
c = float(input("c -> "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)

print(f'El resultado es {resultado}')

#Ejercicio 2

a = float(input("a ->"))
b = float(input("b ->"))

resultado2 = ((3+5*8) < 3 and (-6/3*4)+2 < 2) or (a > b)

print(f"El resultado es {resultado2}")

#Ejercicio 3 cambiar datos de dos variables

a = input("Ingrese valor de a ")

b = input("Ingrese valor de b ")

a, b = b, a

print(f"el nuevo valor de a es {a}")
print(f"el nuevo valor de b es {b}")
