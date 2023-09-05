m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in range(m):
    if all(x % 2 == 0 for x in matrix[i]):
        result.append(i)

if not result:
    print(0)
else:
    print(result[-1] + 1)