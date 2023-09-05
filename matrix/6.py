m=int(input())
n=int(input())
q=int(input())
numbers=[m]
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)
for i, number in enumerate(numbers):
    matrix[0][i] = number
for i in range(1, m):
    for j in range(n):
        matrix[i][j] = matrix[i - 1][j] * q
print(*matrix)