matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for array in range(len(matrix[0])):
    avg_array = sum(row[array] for row in matrix) / len(matrix)
    count = 0
    for row in matrix:
        if row[array] > avg_array:
            count += 1
    print(count)