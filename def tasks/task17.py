from math import pi


def cmdTriangle(a, b, c):
	if (a + b <= c) or (b + c <= a) or (a + c <= b):
		return False
	return True
def sRectangle(a, b):
	return a * b

def sCircle(r):
	return r * r * pi

def sTriangle(a, b, c):
	p = (a + b + c) / 2
	return (p*(p - a)*(p - b) * (p - c)) ** 0.5

s = input("enter a type of a figure(triangle, rectangle, or circle):\n")

if s == "triangle":
	a, b, c = map(int, input("Enter 3 numbers:\n").split())
	if cmdTriangle(a, b, c):
		print(sTriangle(a, b, c))
	else:
		print("this triangle is impossible")


if s == "rectangle":
	a, b = map(int, input("Enter 2 numbers:\n").split())
	print(sRectangle(a, b))

if s == "circle":
	r = int(input("enter a radius:\n"))
	print(sCircle(r))