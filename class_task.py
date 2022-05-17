class task:
    def __init__(self,game,colour):
        self.game = game
        self.c = colour

    def display(self):
        print("I love playing",self.game)
        print(self.c,"is my fav colour")

tas = task(input("Enter your fav Game: ") , input("Enter your Fav Colour: "))
tas.display()