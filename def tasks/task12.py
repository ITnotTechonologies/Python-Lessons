def find(arr, x):
	for i in arr:
		if i == x:
			return True
	return False

def year(num_month):
	hesh = {
		"winter":[1, 2, 12],
		"spring":[3, 4, 5],
		"summer":[6, 7, 8],
		"autumn":[9, 10, 11],
			}
	for i in hesh:
		if find(hesh[i], num_month):
			return i
	return "NONE"

num_month = int(input("enter month nuber:\n"))

print(year(num_month))
