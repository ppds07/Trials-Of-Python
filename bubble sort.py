A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    min = i
    for j in range(i+1, len(A)):
        if A[min] > A[j]:
            min = j

A[i], A[min_idx] = A[min], A[i]


print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]),
