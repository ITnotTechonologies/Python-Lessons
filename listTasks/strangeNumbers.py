# 9

arr = [1, 1]
el = 0

while el < 56:
	el = arr[-1] + arr[-2]
	arr.append(el)
	
for i in arr:
	if i < 5:
		print(i, end = ' ')

