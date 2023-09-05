m=int(input())
n=int(input())
matrix=[m]
result=[]
for i in range(m):
    if i % 2 == 0:
        result.extend(matrix[i])
print(*result)