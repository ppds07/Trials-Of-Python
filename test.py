def char_mix_up(a,b):
    
    new_a = a[:1]+b[:1]
    new_b = a[1:2]+b[1:2]
    new_c = a[2:3]+b[2:3]
    new_d = a[3:4]+b[3:4]
    print(new_a+new_b+new_c+new_d)
    
a = input("Enter a variable")
b = input("Enter another variable")
char_mix_up(a,b)