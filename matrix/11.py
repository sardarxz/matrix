m=int(input())
n=int(input())
matrix=[]
for i in range(m):
    row=[]
    if i % 2 == 0:
        for j in range(n):
            row.append(matrix[i][j])
    else:
        for j in range([i][::-1]):
            row.append(matrix[i][j])
print(matrix)