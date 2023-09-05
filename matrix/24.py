matrix=[[1,2,3],[4,5,6],[7,8,9]]
a=[]
for array in range(len(matrix[0])):
    sum=0
    for j in range(1,len(matrix)):
        if matrix[j][array]>matrix[sum][array]:
            sum=j
    a.append(matrix[sum][array])
print(a)