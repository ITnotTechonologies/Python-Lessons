#5

def upToLowF(string):
	return chr(ord(string[0]) + 32) + string[1::]


def lowToUpF(string):
	return chr(ord(string[0]) - 32) + string[1::] 

languages = ['Georgian', 'Estonian', 'Ukrainian']

languages[-1] = upToLowF(languages[-1])

print(languages[-1])

print(lowToUpF(languages[-1][::-1]))