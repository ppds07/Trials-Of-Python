n = input("Enter a String")
v = "aAeEiIoOuU"
c=0
for i in n:
    if i in v:
        c=c+1
print("No Of Vowels: ",c)
print("No Of Consonants: ",len(n)-c)
