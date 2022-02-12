def make_shirt(size, text):
	print('Size of your shirt:{}'.format(size))
	print('Text on your shirt:{}'.format(text))

make_shirt('l', 'I hate c++')

make_shirt(text = 'I love C++', size = 'XL')

make_shirt(**{'text':'I love/hate C++', 'size':'oversize'})