value = 56

if value:
    print("koala")
    print("kookaburra")
elif value > 50:  # else if
    print("wallaby")
    print("wombat")
else:
    print("kangaroo")
    print("platypus")
    print("quokka")

print("All done.")

#  if else elif while for with def class try except finally

#  x is False if:
#  x == False
#  x == None
#  x == 0  (if x is a number)
#  len(x) == 0  (if x is a "container" -- anything with multiple elements)
# containers: str bytes list tuple dict set frozenset
#  True False
#  True == 1
#  False == 0
debug = True

color = "red" if debug else "green"
print("color: {}".format(color))

country = 'France'
print("euro" if country == 'France' else "dollar")

if country == 'France':
    print('euro')
else:
    print('dollar')

#  == != > < >= <= is

if country is None:   # if country == None
    print("blah")

#  and or
if (value > 50) and (country == 'Burkina Faso'):
    print("yee haaaa")
# not
if (value > 50) or (country == 'Burkina Faso'):
    print("well, doggies")

x = 50
print(bool(x))
print(not bool(x))









