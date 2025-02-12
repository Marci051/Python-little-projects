#simple function
# def greet():
#     print("Hello ")
#     print("How are you? ")
#     print("Is the weather nice? ")

# greet()


#function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print(f"Is the weather nice {name}?")

# greet_with_name(input())

def greet_with_name(name,location):
    print(f"Hello {name} in {location}")
    print(f"How are you {name} in {location}?")
    print(f"Is the weather nice {name} in {location}?")

greet_with_name(input("name? "),input("location? "))