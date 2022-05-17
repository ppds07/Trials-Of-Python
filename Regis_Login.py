print("Register Please")
usr=input("Enter User Name: ")
email=input("Enter E-Mail ID: ")
passwd=input("Enter Password: ")
print("Registered Successfully")
print("\n")
print("*****LOGIN*****")
while True:
    usrname = input("Enter User Name: ")
    password = input("Enter Password: ")
    if usrname==usr and password==passwd:
        print("Login Successful")
        break
    else:
        print("Login Failed")
