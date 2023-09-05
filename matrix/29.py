matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    array = sum(row) / len(row)
    count = 0
    for element in row:
        if element < array:
            count += 1
    print(count)