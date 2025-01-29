class Cat:
    def __init__(self):
        self.catsound="Meow"
    def sound(self):
       print("This is cat sound:",self.catsound)
class Dog:
    def __init__(self):
        self.dogsound="Bark"
    def sound(self):
       print("This is dog sound:",self.dogsound)
for animal in [Cat(),Dog()]:
    animal.sound()