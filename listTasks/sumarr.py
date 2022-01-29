# 8

# Первая функция работает для массивов с количевством элементов не больше 1000
# Обычно этого хватает, но дальше есть универсальная функция
def sumArr(arr):
	if len(arr) < 2:
		return arr[0]
	else:
		return sumArr(arr[1::]) + arr[0]

# Функция далее будет работать при всех условиях

# def sumArr(arr):
# 	if len(arr) < 1:
# 		return 0
# 	else:
# 		sm = 0
# 		for i in arr:
# 			sm += i
# 		return sm

arr = []

arr = list(map(int, input().split()))

print(sumArr(arr))