matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_sum = []
for array in range(len(matrix[0])):
    s = 0
    for i in range(1, len(matrix)):
        if matrix[i][array] > matrix[s][array]:
            s = i
    max_sum.append(matrix[s][array])
max_sum = min(max_sum)
print(max_sum)