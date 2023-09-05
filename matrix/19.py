M=int(input())
N=int(input())
matrix = [[1,2,3,4],[5,3,4,5],[2,1,3,4]]
sum = []
for row in matrix:
    s = 0
    for element in row:
        s += element
    sum.append(s)
for row_sum in sum:
    print(row_sum)