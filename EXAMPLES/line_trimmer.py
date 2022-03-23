#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # <1>


mary = trimmed('../DATA/mary.txt')
print("type(mary): {}\n".format(type(mary)))

for trimmed_line in mary:  # <2>
    print(trimmed_line)
