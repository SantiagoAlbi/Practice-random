
def factorial(num):
    if num>0:
        resultado = num * factorial(num-1)
    else:
        resultado = 1
    return resultado

print(factorial(5))