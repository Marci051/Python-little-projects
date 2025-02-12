print("welcome to the restaurant!")
size = input("which size of pizza do u want? L , M or S?")
bill = 0
add_pepperoni = input("do u want pepperoni? y or n.")
extra_cheese = input("do u want extra cheese?y or n.")

if size == "l" or "L":
    bill = 25
    if add_pepperoni == "y":
        bill +=3
elif size== "M" or "m":
    bill = 20
    if add_pepperoni == "y":
        bill +=3
else:
    bill = 15
    if add_pepperoni == "y":
        bill +=2
if extra_cheese == "y":
    bill +=1   

print(f"tital bill is: {bill}")



