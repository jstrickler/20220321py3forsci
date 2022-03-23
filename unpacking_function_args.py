
def greet(greeting, whom):
    print(greeting, whom)

greet("Hello", "world")
greet("Hi", "Mom")

data = ["Howdy", "Partner", 'wombat']
greet(data[0], data[1])
greet(*data[:2]) # unpack list into individual arguments

