fruits = ["pomegranate   ", "cherry", "apricot", "Apple", "LIME",
"lemon   ", "Kiwi", "ORANGE", "lime", "Watermelon", "guava", "    date    ",
"Papaya", "FIG", "   pear", "banana", "Tamarind", "Persimmon", "apple",
"elderberry", "   peach", "   APPLE", 'PEACH', 'Lemon', "BLUEberry", "lychee", "GRAPE", "date" ]

unique_fruits = {f.strip().lower() for f in fruits}
print("unique_fruits:", unique_fruits)
sorted_fruits = sorted(unique_fruits)
print("sorted_fruits: {}\n".format(sorted_fruits))

f1 = [f.strip().lower() for f in fruits]
print("f1: {}\n".format(f1))

fgen = (f.strip().lower() for f in fruits)
print("fgen: {}\n".format(fgen))

for fruit in fgen:
    print(fruit)
print()



