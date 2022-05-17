class employee:

    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.salary = input("Enter Your Salary: ")

    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)

s = employee()
s.display()