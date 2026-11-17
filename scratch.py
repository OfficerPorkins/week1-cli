class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def learn(self, trick):
        self.tricks.append(trick)

rex = Dog("Rex")
fido = Dog("Fido")
rex.learn("sit")

print(rex.tricks)
print(fido.tricks)
print(fido.learn("roll over"))