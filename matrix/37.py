m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

row = set([matrix[i][n - 1] for i in range(m)])
sum = 0
for j in range(n - 1):
    column = set([matrix[i][j] for i in range(m)])
    if column == row:
        sum += 1

print(sum)