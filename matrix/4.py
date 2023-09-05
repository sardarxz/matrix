m=int(input())
n=int(input())
M=[n]
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(n)
for number in M:
    array = M.index(number)
    matrix[array][n - 1] = number
print(matrix)