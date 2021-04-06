
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

#print(factorial(100))

def matrix_multiply(matrix_size, matrix_a, matrix_b):
    results_matrix = [] 
    ans = 0 
    for i in range(matrix_size):
        new_matrixrow = []
        for j in range(matrix_size):
            for h in range(matrix_size):
                product = matrix_a[i][h] * matrix_b[h][j]
                ans += product
            new_matrixrow.append(ans)
            ans = 0
        results_matrix.append(new_matrixrow)
    return results_matrix       