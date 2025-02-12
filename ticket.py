print("Welcome to the rollercoaster! ")
height = int(input("what's ur height in cm?"))
bill = 0

if height>=120:
    age = int(input("how old are u?"))
    if age < 12:
        bill = 5
        print ("child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("adult tickets are $12.")

    want_photos = input("do u want a photo taken? Y or N.")
    if want_photos == "Y" or want_photos =="y":
        bill +=3
        print(f"total bill is {bill}")
    else:
        print(f"total bill is {bill}")
else:
    print("u can't ride.")


