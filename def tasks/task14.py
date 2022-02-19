def f(n):
	if n % 2 == 0:
		return "Paired"
	return "Unpaired"

n = int(input("Enter a number:\n"))

print(f(n))