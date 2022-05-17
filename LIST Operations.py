#List Operation With String []

cars=['Ford','Honda','Tata','Kia','Nissan']

#Length
print("Length is: ",len(cars))

#Positive Indexing
print("+ve Indexing of 3: ",cars[3])

#Negative Indexing
print("-ve Indexing of -4: ",cars[-4])

#Change/Replace
cars[3]="Rolls Royce"
print("Replaces Kia",cars)

#Add/Append
cars.append("Maruti Suzuki")
print("Modified List: ",cars)

#Concatenation (MERGING)
models = ['Focus','Civic','Altroz','Boattail','GTR']
print(cars + models)

#Repeat
print(cars * 2)

#Delete
del cars[3]
print("Deleted 4th Company: ",cars)
