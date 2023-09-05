m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

row = 0
for row in matrix:
    if all(row[i] <= row[i + 1] for i in range(n - 1)) or all(row[i] >= row[i + 1] for i in range(n - 1)):
        row = min(row, min(row))

print(row)