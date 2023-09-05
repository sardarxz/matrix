m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

row = 0
for i in range(m):
    sum = max(matrix[i])
    max_row = min(matrix[j][i] for j in range(m))
    if sum == max_row:
        row = sum

print(row)