
from tqdm import tqdm
import random
from . import util
from . import log
from . import pypy
from . import config
from .timer import Timer

TEST_RANGE = config.CONFIG["test range"]

def run():
    data = log.read_file()
    tests = [factorial_test(), matrix_multi_test(), adding_numbers_test(), dict_inset_test(), dict_remove_test()]
    for tst in tests:
        if tst.name in data.keys():
            data[tst.name]["pypy"] = tst.avg
        else:
            data[tst.name] = {}
            data[tst.name]["pypy"] = tst.avg

    log.write_file(data)

def factorial_test():
    results_py = []
    for _ in tqdm(range(TEST_RANGE)):
        with Timer() as t:
            pypy.factorial(500)
        results_py.append(t.secs)

    return util.singelResult("factorial", results_py)

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

    return util.singelResult("matrix multiply", results_py)


def adding_numbers_test():
    results_py = []
    for _ in tqdm(range(10)):
        with Timer() as t:
            pypy.adding_numbers(10000)
        results_py.append(t.secs)

    return util.singelResult("adding numbers", results_py)


def dict_inset_test():
    results = []
    for _ in tqdm(range(100)):
        with Timer() as t:
            pypy.dict_inset(100000)
        results.append(t.secs)

    return util.singelResult("dictionary insert", results)


def dict_remove_test():
    results = []
    for _ in tqdm(range(100)):
        dic_ = pypy.dict_inset(100000)
        with Timer() as t:
            pypy.dict_remove(dic=dic_)
        results.append(t.secs)

    return util.singelResult("dictionary remove", results)



if __name__ == '__main__':
    run()
