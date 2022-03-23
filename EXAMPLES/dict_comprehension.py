#!/usr/bin/env python
import os

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.lower(): len(a) for a in animals}  # <1>

print(d, '\n')

words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']

# d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # <2>
#
# for word, word_signature in d.items():
#     print(word, word_signature)

files = ['alice.txt', 'parrot.txt', 'words.txt', 'mary.txt', 'knights.txt']
file_names = os.listdir('../DATA')
file_sizes = {file_name: os.path.getsize(os.path.join('../DATA', file_name)) for file_name in file_names if file_name.endswith('.txt')}

print(file_sizes)


