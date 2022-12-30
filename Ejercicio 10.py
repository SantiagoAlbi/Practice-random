#Ejercicio 10: Hacer una cadena por teclado, luego crear una lista sin repetir caracteres

cadena = input("Digitar una cadena: ")

lista = []

for i in cadena:
    if i not in lista:  #Si el caracter no esta en la lista, se agrega
        lista.append(i)

print(lista)