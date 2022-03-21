
actor = "Chris Hemsworth"

a = actor.upper()
print("a: {}".format(a))

c = actor.count('h')
print("c: {}".format(c))

#   actor.upper()   len(actor)
print(actor.count('ems'))
print("actor: {}".format(actor))
print(actor.lower().count('h'))

print(actor.startswith('Chris'), actor.startswith('Liam'))
#  .endswith("...")
print("ems" in actor, "wombat" in actor)

pos = actor.find('ems')
print("pos: {}".format(pos))
pos = actor.find('wombat')
print("pos: {}".format(pos))

date = '2022-3-27'

fields = date.split('-')
print("fields: {}".format(fields))

s = "Python is the best language"
print(s.split())

s = "        Python is the best language         "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

m = "    MONKEY CHANDELIER     "
m2 = m.strip().lower()
print(m2)

m3 = m.strip().title()
print(m3)













