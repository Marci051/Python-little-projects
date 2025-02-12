row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]

map = [row1, row2, row3]

print("     1     2     3")
print(f"1 {row1}\n2 {row2}\n3 {row3}")

position_string = input("where do u want to put the treasure? (the numbers with a space between)\n")
position_list = position_string.split(" ")

#map[int(position_list[1])-1]
map[int(position_list[1])-1][int(position_list[0])-1] = " X"

print("     1     2     3")
print(f"1 {row1}\n2 {row2}\n3 {row3}")
