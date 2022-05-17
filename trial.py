a = input("Enter a Word")
length: int = len(a)
print(length)
c = ""
d = ""
for i in range(0, length):
    le: int = (i)
    b = a[le]
    if b == " ":
        c = a[0,le]
        d = a[i,length]
print("New Sentence: ", d + c)
