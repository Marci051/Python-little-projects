def min_filled_seats(n):
    seats = [0] * (n + 1) 
    filled_count = 0

    for i in range(1, n + 1): 
        found_seat = False
        for j in range(i, n + 1, i): 
            if seats[j] == 0: 
                seats[j] = 1  
                filled_count += 1
                found_seat = True
                break 

    return filled_count

results = {}
for n in range(1, 11):
    results[n] = min_filled_seats(n)

for n in range(1, 11):
    print(f"n = {n}: Min filled seats = {results[n]}")

###############