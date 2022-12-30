#Ejercicio 11, hacer simulador de agenda de contacto

agenda = {}

while True:
    print("t\ MENU")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos")
    print("4. Salir")
    opcion = int(input("Digite una opcion del Menu: "))

    print()

    if opcion == 1:
        nombre = input("Nombre del Contacto: ")
        telefono = input("Numero de telefono: ")

        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado")
        else:
            print("Ese nombre de contacto ya existe")

    elif opcion == 2:
        nombre = input("Nombre de contacto")

        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto eliminado")
        else:
            print("Contacto inexistente")
    elif opcion == 3:
        print("Agenda de contactos:")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")

    elif opcion==4:
        print("Gracias por utilizar su agenda de contactos")
        break

    else:
        print("SE equivoco de opcion de menu")

print()