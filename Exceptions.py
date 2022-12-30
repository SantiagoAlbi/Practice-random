age = int(input("Age: "))
print(age)

print("........")

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

