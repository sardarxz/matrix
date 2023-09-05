m = int(input())
n = int(input())
matrix = [[1,2,3,4],[4,2,3,1],[3,4,1,2]]
sum = []
for i in range (0,n,2):
    row_sum = 0
    for j in range (m):
        row_sum += matrix[i][j]
    sum.append(row_sum / m)
for number in sum:
    print(number)