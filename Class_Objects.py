class student:
    #init is used to initialize the variables
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

#to make a constructor / object of class.

s = student(input("enter your Name") , int(input("Enter Your Age")))
s.display()