d1 = dict()
d1['spam'] = 12
d1['ham'] = 99
d1['eggs'] = 3
print("d1: {}".format(d1))

values = {'m': 66, 'b': 31, 'e': 98, 'a': 423}
d2 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

airports['YKF'] = "Kitchener/Waterloo"
airports['IAD'] = "Washington, DC"
print("airports: {}\n".format(airports))

print("airports['MCI']: {}\n".format(airports['MCI']))

print("airports.get('LAX'): {}\n".format(airports.get('LAX')))
print("airports.get('LAX', 'NOT FOUND'): {}\n".format(airports.get('LAX', 'NOT FOUND')))

more_airports = [
    ('JFK', 'NYC Kennedy'),
    ('LAX', 'Los Angeles'),
    ('BOS', 'Boston'),
    ('MCO', 'Disney'),
]

for code, name in more_airports:
    print(airports.setdefault(code, name))

print("airports: {}\n".format(airports))

del airports['SMF']
print("airports: {}\n".format(airports))

print("len(airports): {}\n".format(len(airports)))

for code, name in airports.items():
    print(code, name)
print('-' * 60)

print(airports.items())
print(airports.keys())
print(airports.values())
print('-' * 60)













