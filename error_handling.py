import sqlite3

file_path = "DATA/fun_with_wombats.txt"

try:
    with open(file_path) as wombats_in:
        contents = wombats_in.read()
except (FileNotFoundError, PermissionError) as err:
    print(err)

with open('DATA/breakfast.txt') as breakfast_in:
    all_lines = [line.rstrip() for line in breakfast_in]

try:
    print(all_lines[22])
except IndexError as err:
    print(err)

nums = [800, 17, 80, 0, 1000, 32, 255, "abc", 400, 5, 5000]

for num in nums:
    try:
        result = 1234 / num
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("WRONG DATA TYPE!!")
    except Exception as err:
        print(err)
    else:
        print("result:", result)

conn = None
try:
    with sqlite3.connect('DATA/db/wombats.db') as conn:
        cursor = conn.cursor()
    #  make queries now
except sqlite3.Error as err:
    print(err)
    exit() # exit script
finally:  # whether errors raised or not
    if conn is not None:
        conn.close()




print("All done.")
