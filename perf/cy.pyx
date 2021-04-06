def primes(int nb_primes):
    cdef int n, i, len_p
    cdef int p[1000]
    if nb_primes > 1000:
        nb_primes = 1000
    len_p = 0
    n = 2
    while len_p < nb_primes:
        for i in p[:len_p]:
            if n % i == 0:
                break
        else:
            p[len_p] = n
            len_p += 1
        n += 1
    result_as_list  = [prime for prime in p[:len_p]]
    return result_as_list


def factorial(int num):
    if num == 0:
        return 1
    else:
        return factorial(num-1)*num


def matrix_multiply(int matrix_size, matrix_a, matrix_b):
    results_matrix = [] 
    cdef int ans = 0 
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