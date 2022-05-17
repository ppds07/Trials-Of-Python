def msort(a):
	if len(a) > 1:
		mid = len(a)//2
		L = a[:mid]
		R = a[mid:]
		msort(L)
		msort(R)

		i = j = k = 0
    
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				a[k] = L[i]
				i += 1
			else:
				a[k] = R[j]
				j += 1
			k += 1
      
		while i < len(L):
			a[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			a[k] = R[j]
			j += 1
			k += 1


def printList(a):
	for i in range(len(a)):
		print(a[i], end=" ")
	print()

if __name__ == '__main__':
	a = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(a)
	msort(a)
	print("Sorted array is: ", end="\n")
	printList(a)