def spiral(A):
    result = []
    for i in range(len(A)):
        if i % 2 == 0:
            result.extend(A[i])
    else:
        result.extend(A[i][::-1])
    return result
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiral(A))