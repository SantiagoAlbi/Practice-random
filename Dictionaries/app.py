#Jamas se repite el dato, y puede ser cualquier dato, string, boolean, float, etc...
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate")) #El resultado es que no esta ese item.

#Agregar un valor
customer["birthdate"] = "Jan 1 1980"
print(customer)