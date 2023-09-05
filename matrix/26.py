matrix=[[1,2,3],[4,5,6],[7,8,9]]
min_sum=1
row=0
for j in range(len(matrix[0])):
    sum=1
    for i in range(1,len(matrix)):
        sum*=matrix[i][j]
        if sum<min_sum:
            min_sum=sum
            row=j
print(row,min_sum)