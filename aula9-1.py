# Exeercicio do polimorfismo

class Mamifero:
    def som(self):
        print('Emitir um som')

class Homem(Mamifero):
    def som(self):
        print('Oi')
    
class Cachorro(Mamifero):
    def som(self):
        print('Wuff Wuff')

class Gato(Mamifero):
    def som(self):
        print('Meawww')

mamifero = Mamifero()
mamifero.som()

animais = [Homem(), Cachorro(), Gato()]
for animal in animais:
    animal.som()