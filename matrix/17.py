m=int(input())
n=int(input())
k=int(input())
matrix=[[2,3,4,5],[5,4,2,4],[2,8,3,5]]
s=0
p=1
for i in range(n):
    s+=matrix[k-1][i]
    p*=matrix[k-1][i]
print(s,p)