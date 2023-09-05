m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

result = []
for j in range(n):
    if all(x % 2 != 0 for x in [matrix[i][j] for i in range(m)]):
        result.append(j)

if not result:
    print(0)
else:
    print(result[0] + 1)