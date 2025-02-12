year = int (input ("which year do u want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it's a leap year.")
        else:    
            print("it's not a leap year.")
    else:
        print("it's a leap year.")
else:    
    print("it's not a leap year.")    
            