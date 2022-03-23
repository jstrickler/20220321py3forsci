flopsy_countries = ['Bolivia', 'Spain', 'Burkina Faso', 'Iceland', 'Canada', 'Switzerland',
                    'Poland', 'Ukraine', 'Russia', 'China', 'Gambia']

mopsy_countries = ['Spain', 'France', 'Spain', 'Spain', 'Canada', 'China', 'Eswatini',
                   'Morocco', 'Afghanistan', 'Bhutan', 'Iceland', 'Japan', 'China']

flopsy = set(flopsy_countries)
mopsy = set(mopsy_countries)
flopsy.add('Gambia')
flopsy.add('New Zealand')
mopsy.add('Peru')
mopsy.add('Peru')

print("flopsy: {}\n".format(flopsy))
print("mopsy: {}\n".format(mopsy))

print("Common:", flopsy & mopsy)  # intersection
print("Not common:", flopsy ^ mopsy)  # xor
print("All:", flopsy | mopsy)  # union
print("just Flopsy:", flopsy - mopsy)
print("just Mopsy:", mopsy - flopsy)

