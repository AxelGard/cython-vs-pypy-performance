


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


def adding_numbers(int range_):
    cdef long tot = 0
    cdef long i, j = 1
    for i in range(1, range_):
        for j in range(1, range_):
            tot += i + j
    return tot


cdef double f(double x) except? -2:
    return x ** 2 - x

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx


def is_in_seq(seq, int val):
    cdef int val_
    for val_ in seq:
        if val_ == val:
            return True
    return False
