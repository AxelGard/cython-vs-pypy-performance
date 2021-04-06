#from . import config
from tqdm import tqdm
import random
from . import cy
from . import util
from . import log
from . import pypy

from .timer import Timer



__version__ = "0.1.0"

TEST_RANGE = 10**5

def main():
    fac = factorial_test()
    print(f"factorial test PYPY:{fac[0]}")
    print(f"factorial test Cy  :{fac[1]}")
    print("\n")
    
    mat = matrix_multi_test()
    print(f"matrixmultiply test PYPY:{mat[0]}")
    print(f"matrixmultiply test Cy  :{mat[1]}")

def factorial_test():
    results_py = []
    for _ in tqdm(range(TEST_RANGE)):
        with Timer() as t:
            pypy.factorial(500)
        results_py.append(t.secs)

    results_cy = []
    for _ in tqdm(range(TEST_RANGE)):
        with Timer() as t:
            cy.factorial(500)
        results_cy.append(t.secs)

    return avg(results_py), avg(results_cy)

def matrix_multi_test():

    mat_size = 3
    range_ = 10

    results_py = []
    for _ in tqdm(range(TEST_RANGE)):
        a = util.random_matrix(mat_size, range_=range_)
        b = util.random_matrix(mat_size, range_=range_)
        with Timer() as t:
            pypy.matrix_multiply(mat_size, a, b)
        results_py.append(t.secs)

    results_cy = []
    for _ in tqdm(range(TEST_RANGE)):
        a = util.random_matrix(mat_size, range_=range_)
        b = util.random_matrix(mat_size, range_=range_)
        with Timer() as t:
            cy.matrix_multiply(mat_size, a, b)
        results_cy.append(t.secs)

    return avg(results_py), avg(results_cy)


def avg(lst):
    tot_sum = 0
    for item in lst:
        tot_sum += item
    return tot_sum / len(lst)


if __name__ == '__main__':
    #if config.CONFIG['debug']:
    #print(cy.primes(100))
    main()
