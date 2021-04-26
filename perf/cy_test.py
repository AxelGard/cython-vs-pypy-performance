
from tqdm import tqdm
import random
import util
import log
import cy
import config
from timer import Timer

TEST_RANGE = config.CONFIG["test range"]

def run():
    data = log.read_file()
    tests = [factorial_test(), matrix_multi_test(), adding_numbers_test(), integral_test()]
    for tst in tests:
        if tst.name in data.keys():
            data[tst.name]["cython"] = tst.avg
        else:
            data[tst.name] = {}
            data[tst.name]["cython"] = tst.avg

    log.write_file(data)



def factorial_test():
    results = []
    for _ in tqdm(range(TEST_RANGE)):
        with Timer() as t:
            cy.factorial(500)
        results.append(t.secs)

    return util.singelResult("factorial", results)

def matrix_multi_test():
    mat_size = 9
    range_ = 10

    results = []
    for _ in tqdm(range(TEST_RANGE)):
        a = util.random_matrix(mat_size, range_=range_)
        b = util.random_matrix(mat_size, range_=range_)
        with Timer() as t:
            cy.matrix_multiply(mat_size, a, b)
        results.append(t.secs)

    return util.singelResult("matrix multiply", results)


def adding_numbers_test():
    results = []
    for _ in tqdm(range(10)):
        with Timer() as t:
            cy.adding_numbers(10000)
        results.append(t.secs)

    return util.singelResult("adding numbers", results)


def integral_test():
    results = []
    for _ in tqdm(range(10)):
        with Timer() as t:
            cy.integrate_f(0.0, 10000, TEST_RANGE)
        results.append(t.secs)
    return util.singelResult("integral", results)



if __name__ == '__main__':
    run()
