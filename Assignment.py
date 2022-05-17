
print("Press Enter to Begin")
print("Press Ctrl+C to Exit")
a=True
while a==True:
    try:
        input()
        print("Ready to Play Game")
    except KeyboardInterrupt:
         print("You exit, Login Again")
         a=False
