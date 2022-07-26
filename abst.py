from abc import ABC  
class Polygon(ABC):
    def sides(self):
        pass 

class Triangle(Polygon):
    def sides(self):
        print("triangle has 3 sides")

class Square(Polygon):
    def sides(self):
       print("square has 4 sides")

class Pentagon(Polygon):
    def sides(self):
        print(" pentagon has 5 sides")

t = Triangle()
t.sides()

s = Square()
s.sides()

p = Pentagon()
p.sides()