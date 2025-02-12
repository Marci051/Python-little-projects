turtules = [0, 0, 0, 0]
n = len(turtules)
def correction(n):
    while(turtules != [1, 1, 1, 1]):
        for i in range(n):
            if turtules[i] == 0:
                turtules[i] = 1
                break
            else:
                turtules[i] = 0
        print(turtules)