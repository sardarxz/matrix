m,n=map(int,input().split())
matrix=[list(int,input().split()) for _ in range(n)]

row=0
sum=-1
for i in range(m):
    row=matrix[i]
    count=row.count(row[0])
    if count>row:
        row=count
        sum=i
print(sum+1)