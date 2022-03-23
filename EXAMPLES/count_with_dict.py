#!/usr/bin/env python

counts = {}  # <1>
with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip('\n\r')
        if breakfast_item in counts:   # <2>
            counts[breakfast_item] = counts[breakfast_item] + 1   # <3>
        else:
            counts[breakfast_item] = 1 # <4>

for item, count in counts.items():
    print(item, count)

letter_counts = {}
with open("../DATA/words.txt") as words_in:
    for word in words_in:
        first_letter = word[0]
        if first_letter in letter_counts:
            letter_counts[first_letter] += 1
        else:
            letter_counts[first_letter] = 1

def by_value(letter_count):
    letter, count = letter_count
    return count, letter


for letter, count in sorted(letter_counts.items(), key=by_value, reverse=True):
    print(letter, count)

print(letter_counts.items())
