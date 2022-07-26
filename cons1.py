from tkinter import E


class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print("id:%d\nname:%s"%(self.id,self.name))

c1 = Employee(20, "john")
c2= Employee(21,"shri")

c1.display()
c2.display()