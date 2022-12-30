class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.x = 11
print(point1.x)

print(" - - - - - ")

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")

john.talk()

bob = Person("Bob Smithers")
bob.talk()

#VER CONSTRUCTORS PARA ESTE MIDULO
