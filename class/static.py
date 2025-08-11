
#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

#how to create a class <-->What a class is
# initialiZer <constrocture>
# self key what it is :<this>

from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
       

class Human():

    species="h.sapien"
    genus = "homo"
    count= 0
    # the magic level use
    def __init__(self,gender,name):
        print("The initializer wass called")
        self.gender=gender
        self._name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"
        # House method
        # Human.count=Human.count+1
        self.__class__.count=self.__class__.count +1
        
    # the getter
    @property
    def get_name(self):
        now = datetime.now()
        print("Curreent date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} got name from adam")
        return self._name

    def print_self(self):
        print("----------------------")
        print("name",self._name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")
                        
    @classmethod
    def general_info(cls):
        print("Species:",cls.species)
        print("Genus:",cls.genus)
        print ("human count", cls.count)


# adam=Human(name="adam",gender="Male") #object from a class
adam=Human(name="adam",gender="Male")
eve= Human(name="eve", gender= "Female")

#Getter a property of: <name>:
#print(adam.name)

print(adam.get_name)
# @property
print (adam.species)
print(f"The number of humans are {Human.count}")



adam=Human(name="adam",gender="Male")
eve= Human(name="eve", gender= "Female")
adam.general_info()
