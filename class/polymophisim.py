class Shape:
    def __init__(self,name):
        self._name= name

    def describe(self):
        print(f"This is a {self._name}")
    
    def area (self):
        print(f"for {self._name} the area is not implemented")

Shape1= Shape(name="circle")
Shape1.describe()

class Rectangle (Shape):
    def __init__ (self, length, width):
        super().__init__("Rectangle")
        self._width= width
        self._length= length

    def area (self):
        area= self._length* self._width
        print(f"The are is{area}")

class Triangle(Shape):
    def __init__(self,l,w,h):
        super().__init__("Triangle")
        self_l= l
        self_w= w
        self_h= h
        
r1= Rectangle(10,3)
r1.describe()
r1.area()
t1= Triangle(h=1,w=2,l=3)
t1.describe()
t1.area()

print("name is", t1._name)
