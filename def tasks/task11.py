def HTML(teg_name, teg_string):
	return "<{0}>{1}<{0}>".format(teg_name, teg_string)

teg = input("Enter a HTML-teg:\n")
txt = input("Enter a text inside HTML-teg:\n")

print(HTML(teg, txt))

