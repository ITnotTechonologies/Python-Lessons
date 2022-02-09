print("Привет, эта программа, которая будет шифровать поданую строку маленькими латинскими символами в числа за словарём ")
print('Введи: \n EXIT - чтобы завершить выполнение программы, \n HESH - чтобы увидеть словарь по которому происходит шифрование')

hesh = {}

for i in range(97, 123):
	hesh[chr(i)] = str(i ** 2)

# print(hesh)

while True:
	s = input()
	if s == 'EXIT':
		print('Пока!')
		exit()
	if s == 'HESH':
		for i in hesh:
			print('{0}:{1}'.format(i, hesh[i]))
	else:
		s_res = ''
		for i in s:
			s_res += hesh[i]
		print(s_res)


