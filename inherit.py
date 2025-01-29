class Parent:
    def __init__(self):
        self.bignose="5CM"
    def display_parent(self):
        print("This is the parent class")
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.face='redface'
    def display_child(self):
        print("this is the child class")
child=Child()
child.display_parent()
child.display_child()
print(child.bignose)
p=Parent()
ch=Child()
p=ch
