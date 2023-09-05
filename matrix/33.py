matrix = [[1, -2, 3], [4, -5, 6], [7, -8, 9]]

for j in range(len(matrix[0]) - 1, -1, -1):
    s = 0
    p = 0
    for row in matrix:
        element = row[j]
        if element > 0:
            s += 1
        elif element < 0:
            p += 1

    if s == p:
        print(j)
        break
else:
    print(0)