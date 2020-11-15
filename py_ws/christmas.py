s = '*'
# print(s)
for j in range(0, 21, 2):
    space = ' ' * ((21 - j) // 2)
    print(space + s * (j - 1))
for i in range(6):
    print(" " * 8 + "|")
