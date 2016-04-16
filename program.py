import random

#letters
letters_one = ["a", "e", "i", "o", "u"]
letters_two = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "c", "b", "n", "m"]

#to loop
name = ""
length = random.randrange(3,7)
number = 1

#choose first letter
options = [0,1]
option = random.choice(options)
if(option == 1):
	first_letter = random.choice(letters_two)
else:
	first_letter = random.choice(letters_one)
name = name + first_letter

#choose other letters
while (length > number):
	if(option == 0):
		name = name + random.choice(letters_two)
		option = option + 1
		number = number + 1
	else:
		if(number == 2 or number == 4 or number == 6):
			name = name + random.choice(letters_one)
			number = number + 1
		else:
			name = name + random.choice(letters_two)
			number = number + 1

print name


	