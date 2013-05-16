colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print(color)

# Result:
# blue
# green
# red
# yellow


for color in sorted(colors, reverse=True):
    print(color)

# Result:
# yellow
# red
# green
# blue

# You can also create custom sort order
# Python 3 doesn't have comparison functions anymore, it uses key functions.
for color in sorted(colors, key=len):
    print(color)

# Result:
# red
# blue
# green
# yellow
