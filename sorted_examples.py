
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

def ignore_case(fruit):
    sort_key = fruit.lower()
    print(f"comparing {fruit} as {sort_key}")
    return sort_key

f2 = sorted(fruits, key=ignore_case)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def by_len_then_name(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=by_len_then_name)
print("f4: {}\n".format(f4))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_last_name_first_name(person):
    return person[1], person[0]

for person in sorted(people, key=by_last_name_first_name):
    print(person)
print('-' * 60)

f3 = sorted(fruits, key=str.lower)
print("f3: {}\n".format(f3))

for person in sorted(people, key=lambda p: (p[-1])):  # callback -- pass function to other function
    print(person)

#  lambda param ... : return-value

# lambda : 0
# lambda a,b: a + b

def doit(wombat):
    result = wombat(10, 20)
    return result

def add(x, y):
    return x + y

print(doit(add))

def multiply(i, j):
    return i * j

print(doit(multiply))

print(doit(lambda a, b: a / b))

print(add(15, 30))
print(multiply(8, 9))






