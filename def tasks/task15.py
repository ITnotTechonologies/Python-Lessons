
def f(arr):
	return [arr[0], arr[-1]]

arr = []
arr = list(map(int, input("Enter a list of numbers:\n").split()))


print(f(arr))