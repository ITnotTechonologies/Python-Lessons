A = int(input())
B = int(input())

C = 0
j = 1
for i in range(4):

	
	C += B % 10 * j
	B //= 10

	j *= 10

	C += A % 10 * j
	A //= 10

	j *= 10




print(C)