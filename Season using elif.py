month = str(input("Enter Month in short form; EG:August = 'aug'"))
if month=="oct":
    print("Season: Spring")
elif month in ("jan","dec","nov"):
    print("Season: Winter")
elif month in ("mar","apr","may"):
    print("Season: Summer")
elif month in ("jun","jul","aug"):
    print("Season: Rainy")
else:
    print("Invalid Month for Season")
