# 7

def outputArr(arr):
	for i in arr:
		print(i, end = ', ')
	print()

languages_list = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']

print('languages_list:', end = ' ')
outputArr(languages_list)

ll = languages_list
ll.sort()

print('languages_list.sort() :', end = ' ')
outputArr(ll)

print('languages_list.reverse() :', end = ' ')
llr = languages_list
llr.reverse()
outputArr(llr)

print('sorted(languages_list):', end = ' ')
outputArr(sorted(languages_list))


