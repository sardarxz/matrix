M=int(input())
N=int(input())
matrix = [[1,2,3,4],[1,4,1,5],[2,3,1,2],[2,4,2,1]]
sum = []
for i in range(1, M, 2):
    row_sum = 0
    for j in range(N):
        row_sum += matrix[i][j]
    sum.append(row_sum / N)
for number in sum:
    print(number)