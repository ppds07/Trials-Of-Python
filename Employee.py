class employee:
    def __init__(self,name,salary,phno):
        self.name = name
        self.salary = salary
        self.phno = phno

    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print("Phone Number: ",self.phno)

s = employee(input("Name: ") , int(input("Salary: ")) , int(input("Phone Number:")))
s.display()