def sq(a):
    print(a*a)

l1 = [1,2,3,4,5]
sqre = map(sq,l1)
print(set(sqre))
