import random

names_string = input("give me everybody's name, seprated by a comma and an space.")
names = names_string.split(", ")

num_names = len(names)

num = random.randint(0,num_names-1)

print(f"{names[num]} is going to pay the bill")

