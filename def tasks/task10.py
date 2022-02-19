def calculator(a, b, z):
	return eval(f"{a}{z}{b}")


a, b = map(int, input("Enter 2 numbers:\n").split())
z = input("Enter a 'znak':\n")

print(calculator(a, b, z))