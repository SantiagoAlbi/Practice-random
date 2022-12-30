#Diccionarios (Clave: Valor)

diccionario = {"azul": "blue", "rojo":"red", "verde":"green"}


print(diccionario["azul"])

diccionario["amarillo"] = "yellow"

#eliminar elemento

del(diccionario["verde"])
print(diccionario)

#Diccionario 2 ejemplo agenda, diccionarios anidan otros diccionarios, tuplas, listas
#La clave puede ser lo mencionado anteriormente

diccionario2 = {"Alejandro":[22,1.73], "Jose":[21,1.75], "Maria":[22,1.67]}

print(diccionario2)

#Diccionario video 2

equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo", 17: "Mario Mandzukic"}

print(equipo)
print(equipo[10])#paso la clave no el indice

print(equipo.get(6,"no existe jugador con ese dorsal")) #cuando no encuentra la clave, imprime el mensaje escrito.

print(10 in equipo)#dara respuesta TRUE o False

print(equipo.keys())#imprime solo las claves
print(equipo.values())#Imprime solo valores de las claves
print(equipo.items())#para recorrer diccionarios, resultado en tuplas en clave y valor.
print(len(equipo))#cuantos elementos hay en equipo

equipo.clear() #vacia el diccionario.