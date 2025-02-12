import math
def prime_checker(number):
    accumulator = 0
    for i in range(1, number+1):
        if number%i == 0:
            accumulator+=1
    if accumulator == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("check this number: "))
prime_checker(number = n)
