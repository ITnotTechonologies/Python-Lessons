# Животные: создайте список из трех (и более) животных, обладающих общей характе ристикой. 
# Используйте цикл for для вывода названий всех животных.
# • Измените программу так, чтобы вместо простого названия выводилось сообщение, 
# включающее это название, — например, «A dog would make a great pet».
# • Добавьте в конец программы строку с описанием общего свойства. 
# Например, мож но вывести сообщение «Any of these animals would make a great pet!».
animals = ['cat', 'dog', 'parrot', 'fly', 'lion', 'tiger', 'man']

for i in range(len(animals)):
	print(animals[i], end = ' ')
print()
print()

for i in range(len(animals)):
	print('a {} would make a great pet'.format(animals[i]))
print()
# print()

print('all of these animals would make a great pet, but man will be the greates!')

