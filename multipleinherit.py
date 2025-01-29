'''#Parent class1
class Bird:
    def fly(self):
        return "this bird can able to fly"
#parent class 2
class Mammal:
    def walk(self):
        return "This mammal can walk"
#child class
class Bat(Bird,Mammal):
    pass
bat=Bat()
print(bat.fly())
print(bat.walk())'''
class Man:
    def work(self):
        return "Man can work"
class Woman:
    def cook(self):
        return "woman can cook"
class Person(Man,Woman):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        return f"name:{self.name},age:{self.age},gender:{self.gender}"
    def read(self):
        return "books"
person=Person('jyo',21,'F')
print(person.work())
print(person.cook())
print(person.read())
print("************************")
m1=Woman()
m1=person
print(m1.read())
print(person.display())
