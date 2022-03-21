person = "Fred Flintstone"
city = "Bedrock"
value = 38.2832048008224

print(person, city, value)
#  print(str(person) + ' ' + str(city) + ' ' + str(value) + '\n')
print("Next line")
print(person, city, value, sep="#")
print(person, city, value, sep="//")
print(person, city, value, sep="")
print()

print("Part 1")
print("Part 2")
print("Part 3")
print()

print("Part 1", end=' ')
# if ...
#    print(....)
print("Part 2", end=' ')
print("Part 3")

p1 = "Part1"
p2 = "Part2"
p3 = "Part3"
print(p1, " ")    #  str(p1) + ' ' + str(" ") + "\n"
print(p1, p2, p3)
print(p1, end=' ')
if 0:
    print(p2, end=' ')
print(p3)

print(p1, p2, p3, sep=' ', end='\n')
print(p1, p2, p3)
print()

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")  #   f"foo"  f'foo'  f"""foo"""  f'''foo'''

print("value is {}".format(value))
print(f"value is {value}")
print()
print("value is {:.1f}".format(value))
print(f"value is {value:.1f}")



