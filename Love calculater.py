name1 = input("what's ur name?")
name2 = input("what's their name?")

name1.lower()
name2.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

word1 = t + r + u + e


l = name1.count("l") + name2.count("l") 
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

word2 = l + o + v + e


print(f"the percentage of ur love is %{word1}{word2}")
