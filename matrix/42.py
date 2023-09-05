m,n=map(int,input().split())
matrix=[list(int,input().split()) for _ in range(m)]

row=0
for row in matrix:
    if all(row[i]<=row[row+1] for i in range(n-1)):
        row+1
print(row)