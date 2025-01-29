class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"This car is a {self.brand} {self.model}.")
car1=Car("Toyota","Corolla")
car2=Car("Honda","Civic")
car3=Car("Hyundai","xcent")
car1.display_info()
car2.display_info()
car3.display_info()