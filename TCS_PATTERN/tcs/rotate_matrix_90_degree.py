matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix1 = []

for r in range(len(matrix)):
    k = []

    for i in range(len(matrix)):
        k.append(matrix[i][r])

    matrix1.append(k[::-1])

print(matrix1)