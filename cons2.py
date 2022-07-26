# contructor  - non parameterized   
class Employee:
     def __init__(self) :
         print("this is non parameterized constructor")
     def show(self, name):
         print("hello",name)

c1 = Employee()
c1.show("shri")