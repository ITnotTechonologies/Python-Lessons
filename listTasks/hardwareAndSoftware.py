# 6


hardware = ('website', 'page', 'offtop', 'Progger', 'Pogramming language')
software = ['website', 'page', 'offtop', 'Progger', 'Pogramming language']

for obj in hardware:
	print(obj, end = ' ')

print()

for obj in software:
	print(obj, end = ' ')
print()
software[1] = 'c++'

print(software)
try:
	hardware[1] = 'c++'
except:
	print('Упс.. Не вышло')

print(hardware)
