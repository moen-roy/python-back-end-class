class User():
    def __init__(self,name, email,phone,password):
        self._name= name
        self._email= email
        self._phone= phone
        self._password= password

    def say_name (self):
        print (f"My name {self._name}")
        print (f"email is {self._email}")
        print(f"phone number is {self._phone}")

    def login(self):
        for i in range (0,3):
            password= input(f"Enter your password {i}")
            if self._password== password
        
class Employee (User):
     def __init__(self, name, email, phone,password, salary):
        super.__init__(name,email,phone,password)

        self._salary= salary
        password
