def diagonal(A):
    result = []
    for number in range(1, len(A) + 1):
        for row in range(1, len(A) + 1):
            if number == 1 or row == len(A):
                result.append(A[row - 1][number - 1])
    return result
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal(A))