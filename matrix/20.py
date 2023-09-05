m=int(input())
n=int(input())
matrix=[[1,2,3,4],[5,3,4,5],[2,1,3,4]]
sum=[]
for j in range(n):
    s=1
    for i in range(m):
        s*=matrix[i][j]
    sum.append(s)
for row_sum in sum:
    print(row_sum)