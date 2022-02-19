def describePet(animal_type = 'dog', pet_name = 'sharik'):
	print(f"\n I have got a/an {animal_type}")
	print(f"My {animal_type} and his name is {pet_name.title()}")

describePet(pet_name = input(), animal_type = input())
describePet(input())