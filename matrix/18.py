m=int(input())
n=int(input())
k=int(input())
matrix=[[1,2,2,2],[1,1,1,1],[2,2,2,2]]
s=0
p=1
for i in range(m):
    s+=matrix[k-1][i]
    p*=matrix[k-1][i]
print(s,p)