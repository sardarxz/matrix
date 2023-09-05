m=int(input())
n=int(input())
d=int(input())
numbers=[m]
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)
for i, number in enumerate(numbers):
    matrix[i][0] = number
for j in range(1, n):
    for i in range(m):
        matrix[i][j] = matrix[i][j - 1] + d
print(matrix)