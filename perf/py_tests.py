
from tqdm import tqdm
import random
import util
import log
import pypy
import config
from timer import Timer

TEST_RANGE = config.CONFIG["test range"]

def run():
    data = log.read_file()
    tests = [factorial_test(), matrix_multi_test(), integral_test(), list_search_test()]
    for tst in tests:
        if tst.name in data.keys():
            data[tst.name]["py"] = tst.avg
        else:
            data[tst.name] = {}
            data[tst.name]["py"] = tst.avg

    log.write_file(data)

def factorial_test():
    results = []
    for _ in tqdm(range(TEST_RANGE)):
        with Timer() as t:
            pypy.factorial(500)
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
            pypy.matrix_multiply(mat_size, a, b)
        results.append(t.secs)

    return util.singelResult("matrix multiply", results)


def adding_numbers_test():
    results = []
    for _ in tqdm(range(1000)):
        with Timer() as t:
            pypy.adding_numbers(10000)
        results.append(t.secs)

    return util.singelResult("adding numbers", results)


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

def integral_test():
    results = []
    for _ in tqdm(range(10)):
        with Timer() as t:
            pypy.integrate_f(0.0, 10000, TEST_RANGE)
        results.append(t.secs)
    return util.singelResult("integral", results)



def list_search_test():
    results = []
    seq = list(range(2, TEST_RANGE*100))
    seq.append(1)
    for _ in tqdm(range(1000)):
        with Timer() as t:
            pypy.is_in_seq(seq, 1)
        results.append(t.secs)
    return util.singelResult("in list", results)




if __name__ == '__main__':
    run()
