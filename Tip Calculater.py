print("Welcome to the tip calculater. ")
bill= float(input("What was the total bill? $"))

print("what percentage tip would u like to give? 10, 12 or 15.")
tip = ((float(input()))/100)

print("how many people to split the bill? ")
people = float(input())

#there is 2 ways to formatting: (for whatever has output)
#total = "{:.2f}".format(((bill * (tip))+bill) / people)
total = f"{((bill * tip)+bill) / people:.2f}"
print("each person shold pay: $"+total)




