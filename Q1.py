n = int(input("Enter a number: "))
i = n
out = 1
for i in range(1,n+1):
    out = out * i
    i = i+1
print("Factorial :",out)