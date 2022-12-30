#Ejercicio 9: Mostrat frase sin espacios y contar

frase = input("Digite una frase: ")
frase2 = ""

for i in frase:
    if i!=" ":
        frase2 += i

print(frase2)
print(f"Numero de caracteres: {len(frase2)}")