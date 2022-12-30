#Listas parecidas a arreglos o vectores, estructuras de datos flexibles



lista = [1,2,3,4,5, "Alejandro"]

#Imprimir elemento del orden de la lista
print(lista[0])
print(lista[-1])
#Sublistas
print(lista[0:3])
print(lista[2:])

#Cantidad de elementos
print(len(lista))

lista.append(6) #agrega por el final
lista.insert(2,90) #El primer valor es la ubicacion y el segundo es el elemento a agregar
lista.extend([6,7,8])
print(lista.index(5))

print(lista.count(4))

lista.pop(3)
lista.remove(("Alejandro")) #remueve el valor escrito
#lista.clear vacia la lista
lista.reverse()
lista.sort() #ordena la lista (reverse=True
lista2 = [1,2,3,4,5] * 2
print(lista2)
#Concatenar listas con "+"

print(lista)

#Tuplas
#NO se pueden modificar

tupla = (4,"Hola", 6.78,[1,2,3],4 )

print(tupla[2])
print(tupla[1:]) #slicing

print(4 in tupla)#buscar dentro de la tupla

print(tupla.index("Hola"))#Busqueda
print(tupla.count(4))
print(len(tupla))

#transformar tupla en lista

lista2 = list(tupla)
print(lista2)

#Conjuntos - grupo de elementos desordenados, no pueden haber duplicados

conjunto = set() #sin esto es conjunto sino sera un diccionario

conjunto = {1,2,3,"Hola", 4.65} #NO puede haber coleccion dentro de conjuntos, ejemplo:Listas
conjunto.add(5)
conjunto.add("Adios")
conjunto.add("a")

#Eliminar elementos
conjunto.discard(3)

#conjunto.clear
#Buscar elementos
print(4.65 in conjunto)
print(3 not in conjunto)

print(conjunto)

#Unir dos conjuntos , no se repiten elementos

a = {1,2,3}
b = {3,5,6}

c = a | b

#Interseccion

c = a & b

#Diferencia

c = a - b

#Diferencia asimetrica (los que no se repiten)

c = a ^ b
print(c)