class Employee:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
    def display(self):
        print(f"Name:{self.name},Age:{self.age},Position:{self.position}")
emp1=Employee("jyo",20,"Devloper")
emp2=Employee("varsh",21,"Manager")

employees=[emp1,emp2]
for emp in employees:
    emp.display()