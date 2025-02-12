import random

rock = "✊"
paper = "📃"
scissors = "✂️"

choise = int(input("what do u choose? type 0 for rock, 1 for paper, 2 for scissors."))
game_images = [rock, paper, scissors]
# if choise == "0":
#     print(rock)
# elif choise == "1":
#     print(paper)
# elif choise == "2":
#     print(scissors)
# else:
#     print("did u type some thing wrong??")
print(game_images[choise])

computer_choise = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choise])

# if computer_choise == 0:
#     print(rock)
# elif computer_choise == 1:
#     print(paper)
# elif computer_choise == 2:
#     print(scissors)
# else:
#     print("did u type some thing wrong??")

if choise == 0:
    if computer_choise == 0:
        print("draw")
    elif computer_choise == 1:
        print("lose")
    else:
        print("win")
elif choise == 1:
    if computer_choise == 1:
        print("draw")
    elif computer_choise == 2:
        print("lose")
    else:
        print("win")
elif choise == 2:
    if computer_choise == 2:
        print("draw")
    elif computer_choise == 0:
        print("lose")
    else:
        print("win")


    
