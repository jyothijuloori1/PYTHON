class Example:
    def __init__(self,name):
        print(f"First constructor:Hello {name}")
    def __init__(self,age):
        print(f"Second constructor :Age is {age}")

obj=Example(25)

class Example:
    def __init__(self,*args):
        if len(args)==1:
            print(f"Hello {args[0]}")
        elif len(args)==2:
            print(f"Hello {args[0]},you are {args[1]} years old.")
        else:
            print(f"Hello {args[0]},you are {args[1]} years old,you are from {args[2]}")
obj=Example('jyo',21,'Telangana')

class Example:
    def __init__(self,studentName,**kwargs):
        self.studentName=studentName
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']},you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield=kwargs['name']
obj1=Example(studentName='jyo',age=21)

class DestructorExample:
    def __init__(self):
        print(f"object {self.name} is created")
    def __del__(self):
        print(f"object {self.name} is destroyed")
obj2=DestructorExample("sample")
del obj