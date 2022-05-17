
# Number Guessing Game

import random
a = int(input("Enter the Starting Number: "))
b = int(input("Enter the Ending Number: "))
result = random.randint(a,b)
yn = int(input("Enter the number you wished: "))
if result == yn:
    print("Hooray!!, The number is correct")
else:
    print("Sorry!! Try Again")
    print("The Number is: ",result)
