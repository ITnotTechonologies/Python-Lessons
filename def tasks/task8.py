def cmd(a, b, c):
	if (a + b <= c) or (b + c <= a) or (a + c <= b):
		return False
	return True


a, b, c = map(int, input("Введите три стороны треугольника:\n").split())

hesh_ans = {
	True:"Треугольник существует",
	False:"Треугольник не существует"
}

print(hesh_ans[cmd(a, b, c)])