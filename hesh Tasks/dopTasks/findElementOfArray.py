def fHesh(arr):
	h = {}
	for i in range(len(arr)):
		try:
			h[arr[i]] *= 1
		except KeyError:
			h[arr[i]] = 1
			for j in range(len(arr)):
				if arr[i] == arr[j] and i != j:
					h[arr[i]] += 1
	return h

def fArr(s):
	arr = []
	s_el = ''
	for i in s:
		if i == ' ' and s_el != ' ':
			arr.append(s_el)
			s_el = ''
		else:
			s_el += i
	arr.append(s_el)
	return arr



print("Привет, эта программа, которая по заданному массиву определит сколько раз в нём встречается каждый элемент ")
print('Введи: \n EXIT - чтобы завершить выполнение программы')

while True:
	s_inp = input()

	if s_inp == 'EXIT':
		print('Пока!')
		exit()

	else:
		arr = fArr(s_inp)
		hesh_arr = fHesh(arr)

		for i in hesh_arr:
			print('{0}:{1}'.format(i, hesh_arr[i]))

