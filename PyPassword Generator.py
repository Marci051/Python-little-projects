import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z']

# numbers = list(range(0,11))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ]

print("welcome to the password generator.")
nr_letters = int(input("how many letters would u like in ur password?\n"))
nr_symbols = int(input("how many symbols would u like in ur password?\n"))
nr_numbers = int(input("how many numbers would u like in ur password?\n"))

#Easy level 
password = ""
for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
    #or 
    #password += random.choice(letters)

for symbol in range(1,nr_symbols + 1):
    password += random.choice(symbols)

for num in range(1,nr_numbers + 1):
    password += str(random.choice(numbers))

print(password)

#Hard level
password_list = []
for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char
    #or 
    #password += random.choice(letters)

for symbol in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)

for num in range(1,nr_numbers + 1 ):
    password_list += str(random.choice(numbers))

print(password_list)

random.shuffle(password_list)

print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is : {password}")





