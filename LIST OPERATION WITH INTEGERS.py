#List Operation With Numbers []

no=[1,2,3,4,5]

#Length
print("Length is: ",len(no))

#Positive Indexing(Starts from 0)
print("+ve Indexing of 3: ",no[3])

#Negative Indexing(Starts from -1 directly)
print("-ve Indexing of -4: ",no[-4])

#Slicing
print("Slicing: ",no[1:3])

#Change/Replace
no[3]="40"
print("Replaces 4",no)

#Add/Append
no.append("150")
print("Modified List: ",no)

#Concatenation (MERGING)
hundreds = ['100','200','300','400','500']
print(no + hundreds)

#Repeat
print(hundreds * 2,no * 3)

#Delete
del no[3]
print("Deleted 4th number: ",no)
