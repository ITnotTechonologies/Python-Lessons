#3


myBD = 2007

years_list = []

for i in range(5):
		years_list.append(i + myBD)

three = years_list[3]

print("In the {} I was three years old".format(three))

years_list.append(years_list[-1] + 1)

for year in years_list:
	print(year)

print("I was the oldest in {}".format(years_list[-1]))

