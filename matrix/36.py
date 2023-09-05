m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

row = set(matrix[0])
sum = 0
for i in range(1, m):
    if set(matrix[i]) == row:
        sum += 1

print(sum)