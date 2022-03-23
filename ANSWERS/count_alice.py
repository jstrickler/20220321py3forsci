#!/usr/bin/env python
file_path = "../DATA/alice.txt"
alice_lines = 0
total_lines = 0
with open(file_path) as alice_in:
    for line in alice_in:
        if "Alice" in line:
            alice_lines += 1
        total_lines += 1
print("Alice occurred on {} lines out of {} in {}".format(alice_lines, total_lines, file_path))
