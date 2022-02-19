def F(arr):
	for i in arr:
		print("*" * i)


arr = []
arr = list(map(int, input("Enter a list of numbers:\n").split()))

F(arr)