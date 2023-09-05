matrix = [[1, -2, 3], [4, -5, 6], [7, -8, 9]]

for i, row in enumerate(matrix):
    s = 0
    p = 0
    for element in row:
        if element > 0:
            s += 1
        elif element < 0:
            p += 1

    if s == p:
        print(i)
        break
else:
    print(0)