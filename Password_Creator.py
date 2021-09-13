while True:
    n=input("Enter Password")
    if "#" in n and "A" in n and "*" in n:
        print("Password Created")
        break
    else:
        print("Try again")
