class School:
        # no repetition of students
    student_list= {}
        # list of courses
    course_list = []
        # list of teachers
    teacher_list= []

    # the initializer
    def __init__(self,name):

        self._name= name        
       
    def add_student(self,student_name,data):
        self.__class__.student_list[student_name]= data

    def add_course (self,course):
        self.__class__.course_list.append(course)

    def add_teacher(self, teacher):
        self.__class__.teacher_list.append(teacher)
# input for name and region for school
name= input("Enter the enrolling school name: ")
print(" ")

# printing
print("=================================")
print (f"You chose: |{name}|")
print (" ")
print("==================================")

# redefining and calling the class
s_1 =School (name)

class Course(School):
    def __init__(self,course):
        super().__init__(course)
        self._course= course
       
        print ("============================")
        print("Choose your course:")
        print (" ")
        print("1) Software Engineering")
        print (" ")
        print("2) UI/UX")
        print (" ")
        print("3) Cyber Security")
        print (" ")
        print("4) AI")
        print (" ")
        print("5) Devops")
        print ("============================")
    
        course = input("Please enter the course: ")
        if course.isdigit():
         self.course= int(course)
        print(" ")
        print(f"You have selected: |{course}|")
        print("==================================")   
# Course("course")     
 
class Student (Course):
    def __init__(self, username,home,grade,phone,email):
        super().__init__(name)
        self._username= username
        self._home= home
        self._grade= grade
        self._phone= phone
        self._email= email

        # Allowing the user to input the cridentials
        self._username= input("What is your full name? ")
        print(" ")

        grade= input("What are your grades in the interview test? ")  
        print(" ")

        # checks if student is eligble
        if grade.isdigit():
            self._grade = int( grade)
            if self._grade >-1 and  self._grade <101:
                if self._grade <50:
                    print("Sorry! You do not qualify!!")
                    quit()
                else:
                    print(f"Welcome {self._username} to {s_1._name}")
                    print(" ")

                    self._home= input ("Where are you from? ")
                    print(" ")        
                    
                    self._email=input("What is you email? ")
                    print(" ")

                    # converting the phone number to int
                    phone=input ("How can we reach you via phone call? ")  
                    print(" ")                    
  
                    if phone.isdigit():
                        length= len(phone)
                        self._phone= int(phone)
                        #making sure the number has the necessary data   
                        if length <=10 and length > 0:
                            print("=================================")
                            print(f"Thank you for enrolling ni {s_1._name}")   
                            print("=================================")
                        else:
                            print("Must be more than '0' and less than '10'")
                        
                    else:
                        print("Type a number please!")
                        print(" ")
                # making an object of the collected data
                School.student_list[self._username] = {
                        "grade": self._grade,
                        "home": self._home,
                        "email": self._email,
                        "phone": self._phone
                    }
            else:
                print("Must be bellow 100!")
                        
        else:
           print ("Type a number please!")
           quit()
    
    

# # Student("username","home",0,"phone","email")
# print (f"Here is the info you provided: ")
# print(School.student_list)

class Teacher (Student):
    def __init__(self, username, home, grade, phone, email,room,course):
        super().__init__(username,home,grade,phone,email)
        sdft_list= []
        ui_list= []
        cs_list=[]
        ai_list= []
        devops_list= []
        if self.course == 1:
            course= "Software Engineering"
            sdft_list.append(self._username)

        elif self.course ==2:
            course= "UI/UX"
            ui_list.append(self._username)

        elif self.course ==3:
            course= "Cyber security"
            cs_list.append(self._username)

        elif self.course ==4:
            course= "AI"
            ai_list.append(self._username)
        elif self.course ==5:
            course= "Devops"
            devops_list.append(self._username)
        else:

            print("Please chose from the above list of courses")
            print("________________________________________")

            quit()
        print(" ")
        print (f"Welcome to {course} course!")
        print("________________________________________")

Teacher("username","home",0,"phone","email",0,"course")
print (f"Here is the info you provided: ")
print("________________________________________")
print (School.student_list)


