list1 = list()
list3 = []

cities = ['Durham', 'Jersey City', 'Kitchener', 'Atlanta']
cities.insert(0, 'Milton')
cities.insert(2, 'Toronto')
print("cities: {}".format(cities))
cities.append("Boston")
cities.append("San Diego")
print("cities: {}".format(cities))
more_cities = ['NYC', 'Tampa', 'Milwaukee']
cities.extend(more_cities)
print("cities: {}".format(cities))
#  LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)
cities[4] = "Waterloo"
print("cities: {}".format(cities))

pos = cities.index('Boston')
print("pos: {}".format(pos))
del cities[pos]  # delete object with index pos (6)
print("cities: {}".format(cities))

cities.remove('Tampa')
print("cities: {}".format(cities))

c = cities.pop()
print("c: {}".format(c))
print("cities: {}".format(cities))
c = cities.pop(3)
print("c: {}".format(c))
print("cities: {}".format(cities))

#  del LIST[pos]   LIST.remove(value)  LIST.pop(pos=0)
print(cities[0], cities[4], cities[6])
print(cities[len(cities) - 1])
print(cities[-1])

print(cities[0:3])  # first 3
#  start:stop
#  start is beginning pos
#  stop is end pos + 1
#  stop - start is # items
#  start + # items is stop
print("cities[2:5]: {}".format(cities[2:5]))
print("cities[1:6]: {}".format(cities[1:6]))
print("cities[:3]: {}".format(cities[:3]))
print("cities[5:]: {}".format(cities[5:]))
print("cities[-3:]: {}".format(cities[-3:]))

s = "Wankel Rotary Engine"
print(s[7:13])
print(s[-6:])
print(s[:6])
print()

# for VAR in ITERABLE
#     ...
for city in cities:
    print(city)
print()

for city in cities[:4]:
    print(city)
print()









