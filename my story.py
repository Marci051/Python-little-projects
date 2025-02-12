print("Welcome to the Anubis.\nYour mission is to find hostage.")

way = input("in front of u is a mountain. do u want to go left or right?(left , right)\n")
if way.lower() == "right":
    print("a lion ate u.")
elif way.lower()=="left":
    how = input("u came into a river. would u like to swim or wait for a boat? (swim , wait)")
    if how.lower() == "swim":
        print("a corocodile ate u.")
    elif how.lower() == "wait":
        door =input("u came to the final level, there are three doors in front of u. which one do u want to open? (red , blue , green)")
        if door.lower() == "red" or door == "blue":
            print("hostage killed, terrorist wins.")
        elif door.lower() == "green":
            print("u saved the hostage, counter terrorist wins.")
        else:
            print("what???")
    else:
        print("what???")        
else:
    print("what???")

