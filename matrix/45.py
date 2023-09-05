m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

row = 0
for j in range(n):
    column = [matrix[i][j] for i in range(m)]
    if all(column[i] <= column[i + 1] for i in range(m - 1)) or all(column[i] >= column[i + 1] for i in range(m - 1)):
        row = max(row, max(column))

print(row)