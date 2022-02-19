# without function max()
def max2el(a, b):
	if a > b:
		return a
	return b

def max3el(a, b, c):
	return max2el(a, max2el(b, c))


a, b, c = map(int, input("Enter 3 numbers(space-separated):\n").split())


print(max3el(a, b, c))