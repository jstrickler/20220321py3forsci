from math import pi

def get_message():
    return "Hello, Python world"

def nothing():
    pass

r1 = get_message()
r2 = nothing()
print("r1 {}, r2 {}\n".format(r1, r2))

def print_message():
    message = get_message()
    print(message)

print_message()

def circle_area(diameter):
    radius = diameter / 2
    return pi * radius ** 2

print(circle_area(10))

def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 15))
print(rectangle_area(3.5, 4.7))
print()

def greet(whom="world"):
    print("Hello,", whom)

greet('Mom')
greet('Dolly')
greet('esteemed Python programmers')
greet()

def print_line():
    print('-' * 60)

print_line()

