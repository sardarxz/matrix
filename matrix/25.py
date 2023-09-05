matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_sum = 0
row = 0
for i in range(len(matrix)):
    row_max_sum = sum(matrix[i])
    if row_max_sum > max_sum:
        max_sum = row_max_sum
        row = i
print(row, max_sum)