from carddeck import CardDeck
from jokerdeck import JokerDeck

# "client" code
d1 = CardDeck("Betty")
d2 = CardDeck("Beatrice")

print(d1, d2)

# d1.shuffle()
print(d1.dealer)

d1.dealer = "Bronson"
print(d1.dealer)

#
# card = d1.draw()
# print(d1._dealer)  # NAUGHTY!!!

try:
    d1.dealer = 49.7
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)
print()
for i in range(10):
    print(d1.draw())
print(d1)
print(d2)

j1 = JokerDeck("Jimmy")
j1.shuffle()
print(j1.cards)
for i in range(3):
    print(j1.draw())



