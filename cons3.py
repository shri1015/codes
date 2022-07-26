# Constructor - parameterized  
class Employee:
    def __init__(self, name):
        print("this  is parametrized constructor")
        self.name = name
    def show(self):
        print("hello",self.name)

c1 = Employee("shri")
c1.show()

