import random
alpha=['a','b','c','d','e']
r=random.choice(alpha)
guess=input("Guess The Letter between a-f: ")
if guess==r:
    print("Correct guess")
else:
    print("Wrong Guess")
    print("The correct letter is: ",r)
