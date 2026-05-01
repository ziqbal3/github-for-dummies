name = ""
age = ""

def print_name():
    global name, age
    name = input("What's your name? ")
    age = input("What's your age? ")

def introduce():
    print(f"My name is {name}")

print_name()
introduce()
