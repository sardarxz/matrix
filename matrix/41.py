m,n=map(int,input().split())
matrix=[list(int,input().split()) for i in range(m)]

row=0
sum=-1
for j in range(n):
    column=[matrix[i][j] for i in range(m)]
    count=column.count(column[0])
    if count>row:
        row=count
        sum=j
print(sum+1)