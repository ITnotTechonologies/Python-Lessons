# 4

def lowToUpF(string):
	return chr(ord(string[0]) - 32) + string[1::]

things = ['wallet', 'mirror', 'umbrella']

print(lowToUpF(things[2]))

for thing in things:
	print(thing, end = ' ')
print()

things[2] = things[2].upper()

for thing in things:
	print(thing, end = ' ')
print()

things = things[:-1:]

for thing in things:
	print(thing, end = ' ')
print()