name = ""
age = ""

def print_name():
    global name, age
    name = input("What's your name? ")
    age = input("What's your age? ")

def introduce():
    print(f"My name is {name} and I am {age} years old")

print_name()
introduce()
