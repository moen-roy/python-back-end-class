class Rect():
    def __init__(self,length,width):
        if not isinstance(length,(int,float)):
            raise TypeError (f"Expected a number, got {type(length)}")
        if not isinstance(length,(int,float)):
            raise TypeError (f"Expected a number, got {type(width)}")
        
        self._length=length
        self._width=width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self,new_length):
        if not isinstance(new_length,(int,float)):
            #raise TypeError(f"Exptected a number, got {type(new_length)}")
            print("length is not a number")
            return
        self._length=new_length

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,new_width):
        #type of
       
        if not isinstance(new_width,(int,float)):
            #raise TypeError(f"Exptected a number, got {type(new_width)}")
            print("width is not a number")
            return
        self._width=new_width
    


    def area (self):
        return self._length*self._width
    
    def perimeter (self):
        return (2*self._length)+(2*self._width)
    
    def info(self):
        print("Area is", self.area())
        print ("Perimeter is ", self.perimeter())
    
r1= Rect(length=30,width=12)

r1.info()