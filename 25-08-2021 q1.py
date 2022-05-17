n = int(input("Enter a number between 1500 to 2700: "))
c=0
if n >= 1500 and n<= 2700:
    if n%7 == 0 and n%5 == 0:
        print(n," is divisible by 7 and also a multiple of 5")
        c=1
    else:
        if n%7 == 0 and n%5 != 0:
            print(n," is divisible by 7 but not a multiple of 5")
            c=1

        if n%7 != 0 and n%5 == 0:
            print(n," is not divisible by 7 but a multiple of 5")
            c=1
if c!= 1:
    print("The number entered is not between 1500 to 2700")