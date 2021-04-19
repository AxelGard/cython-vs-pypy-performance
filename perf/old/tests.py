
from tqdm import tqdm
import random
from . import cy
from . import util
from . import log
from . import pypy
from . import config
from .timer import Timer

TEST_RANGE = config.CONFIG["test range"]


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

    return util.result("factorial", results_py, results_cy)

def matrix_multi_test():

    mat_size = 9
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

    return util.result("matrix multiply", results_py, results_cy)


def adding_numbers_test():
    results_py = []
    for _ in tqdm(range(10)):
        with Timer() as t:
            pypy.adding_numbers(10000)
        results_py.append(t.secs)

    results_cy = []
    for _ in tqdm(range(10)):
        with Timer() as t:
            cy.adding_numbers(10000)
        results_cy.append(t.secs)

    return util.result("adding numbers", results_py, results_cy)
