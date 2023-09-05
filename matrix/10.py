m=int(input())
n=int(input())
matrix = [m]
result = []
for j in range(n):
    if j % 2 != 0:
        for i in range(m):
            result.append(matrix[i][j])

print(*result)