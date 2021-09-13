from datetime import date
def agecalc(bd):
    today = date.today()
    age = today.year - bd

    print("You are ",age," years old!!")

y = int(input("Enter Birth year: "))
agecalc(y)
