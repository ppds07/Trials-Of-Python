import math
n=int(input("Enter a Number"))
sq=math.sqrt(n)
if n%sq==0:
    print("Yes it is a Perfect Square")
else:
    print("Not a Perfect Square")
