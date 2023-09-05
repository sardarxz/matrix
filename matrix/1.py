m=int(input())
n=int(input())
matrix=[]
for i in range(m):
    array=[]
    for j in range(n):
        array.append(10*(i+1))
    matrix.append(array)
for i in range(n):
    print(matrix[i])