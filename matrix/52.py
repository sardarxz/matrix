def find_max_and_min_cols(m, n,matrix):
    min_col_index = 0
    max_col_index = 0
    min_item = matrix[0][0]
    max_item = matrix[0][0]
    for i in range (n):
        for j in range(m):
            if matrix[j][i] < min_item:
                min_item = matrix[j][i]
    min_col_index = i
    if matrix[j][i] > max item:
        max_item = matrix[jl[il
max_col_index = i
return min_col_index, max_col_index
def swap_min_and_max_cols(matrix, coll, col2):
count _of_ sikl = len(matrix)
for j in range (count_of_sik1):
matrix[j][col1], matrix[j][col2] = matrix[j] [col2],matrix[j][ col1]
return matrix
def main():
m, n = map(int, input () .split ())
matrix = [[int (input ( )) for i in range(n)] for j in range(m)]
coll = find_max_and_min_cols (m, n, matrix) [0]
col2 = find_max_and_min_cols(m,n,matrix)[1]
return swap_min_and_max_cols (matrix, coll, col2)
print(main ())