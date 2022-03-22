file_path = "DATA/mary.txt"

# open and close
mary_in = open(file_path)
# process file here...
mary_in.close()

# read line-by-line
with open(file_path) as mary_in:
    for raw_line in mary_in:
        if "Mary" in raw_line:
            line = raw_line.rstrip()
            print(line)
print('-' * 60)

# read whole file into a string
with open(file_path) as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print('-' * 60)

# read into list of lines with newlines
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read into list of lines without newlines
with open(file_path, "r") as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open("sorted_mary.txt", "w") as mary_out:
    sorted_lines = sorted(all_lines_with_nl)
    for line in sorted_lines:
        mary_out.write(line)

# r  read
# w  write
# a  append
# x  exclusive open (fail if file exists)

with open('DATA/words.txt') as words_in:
    with open('long_words.txt', 'w') as long_words_out:
        with open('short_words.txt', 'w') as short_words_out:
            for word in words_in:
                if len(word) > 20:
                    long_words_out.write(word)
                if len(word) <= 3:
                    short_words_out.write(word)

