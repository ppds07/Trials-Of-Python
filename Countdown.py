import time
def countdown(a):
    while a:
        mins,secs=divmod(a,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\n")
        time.sleep(1)
        a=a-1
    print("Time Up")
a=int(input("Enter time in seconds"))
countdown(a)
