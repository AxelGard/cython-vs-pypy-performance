import copy

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


def adding_numbers(range_):
    tot = 0
    for i in range(1, range_):
        for j in range(1, range_):
            tot += i + j
    return tot


def dict_inset(range_):
    dic = {}
    for i in range(1, range_):
        dic[str(i)] = i
    return dic

def dict_remove(dic):
    keys = [k for k, v in dic.items()]
    for i in keys:
        del dic[i]
    return dic


def f(x):
    return x ** 2 - x


def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
