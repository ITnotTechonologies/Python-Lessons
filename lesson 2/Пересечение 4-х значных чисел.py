def sortArr(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = []
		greater = []
		p = []
		for i in arr:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				greater.append(i)
			else:
				p.append(i)

		return sortArr(less) + p + sortArr(greater)

def find(arr, m):
	for i in arr:
		if i == m:
			return True
	return False

a = int(input())
b = int(input())

arr = []

a1 = 0

for i in range(4):
	a1 = a
	n = b % 10
	b //= 10
	for i in range(4):
		m = a1 % 10
		a1 //= 10
		if m == n and not(find(arr, m)):
			arr.append(m)

arr = sortArr(arr)

if len(arr) == 0:
	print(-1)
	exit()

for i in range(len(arr)):
	print(arr[i], end = ' ')