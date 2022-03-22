
colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

print(len(colors), min(colors), max(colors))
print(sorted(colors))
print(sorted(colors, reverse=True))

unique_colors = set(colors)
print("unique_colors: {}".format(unique_colors))
sorted_unique_colors = sorted(unique_colors)
print("sorted_unique_colors: {}".format(sorted_unique_colors))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))

print("colors: {}".format(colors))
rcolors = reversed(colors)
print("rcolors: {}".format(rcolors))
#print("rcolors[0]: {}".format(rcolors[0]))
# print("len(rcolors): {}".format(len(rcolors)))
for color in rcolors:
    print(color)
print()

combo  = zip(colors, nums)
for color, number in combo:
    print(f"{color:10} {number:5}")
print()
print(list(zip(colors, nums)))
print()

for i, color in enumerate(colors):
    print(i, color)
print()
print(list(enumerate(colors)), '\n')

