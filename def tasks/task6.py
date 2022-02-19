def max2el(a, b):
	if a > b:
		return a
	elif a < b:
		return b
	else:
		print("Equal")
		return b

a, b = map(int, input("Enter 2 numbers(разделенные пробелом):\n").split())

print(max2el(a, b)) 