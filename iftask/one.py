from math import pi

print("Привет, это программа расчитывет длину окружности её площадь")
print("Чтобы выйти введите escape или выйти большими или маленькими буквами")

# f = True 


while True:
	s = input("Радиус окружности : ")
	if s.lower() == 'escape' or s.lower() == "выйти":
		exit()
	try:
		r = float(s)
	except ValueError:
		print('Error!Error')
		print("НУ, русским же языком сказано, напиши число! ЧИСЛО! а ИЗ-ЗА ЭТОГО МНЕ ПРИШЛОСЬ ПИСАТЬ ЕЩЕ 3 СТРОКИ КОДА")
		continue

	# r = int(input('Введите радиус:\n'))

	print('Длина окружности :\n{}'.format(2 * r * pi))
	print('Площадь окружности :\n{}'.format(r ** 2 * pi))

# print(pi)