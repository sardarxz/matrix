matrix=[[1,2,3],[4,5,6],[7,8,9]]
a=[]
for array in matrix:
    sum=0
    for i in range(1,len(array)):
        if array[i]<array[sum]:
            sum=i
    a.append(array[sum])
print(a)