#parent class
class Shape:
    def area(self):
        pass
#child class1
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
#child class2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
s=Square(4)
c=Circle(2)
print(s.area())
print(c.area())