m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

row = 0
for row in matrix:
    if len(set(row)) == n:
        row += 1

print(row)