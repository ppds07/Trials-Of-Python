a=input("Enter brackets")
c=0
if a[0] == "(":
    for i in a:
        if i is "(":
            c=c+1
        elif i is ")":
            c=c-1
    if c==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
