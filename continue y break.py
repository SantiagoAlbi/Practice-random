#Instruccion continue y break es para bucles

for i in range(10): #Obvia la indicacion y continue con la siguiente
    if i == 5:
        continue
    print(i)

print("")

for i in range(10):
    if i == 5:
        break
    print(i)

print("Programa finalizado")

