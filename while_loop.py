i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("What is your name? ")
    if name == '':
        print("Please enter a name")
        continue
    if name == 'q':
        break  # exit loop
    print(f"Hello, {name}")

