#from . import config
import cy
from pypy import factorial
from timer import Timer

__version__ = "0.1.0"

def main():
    #print(cy.primes(100))
    results = []
    for _ in range(10**5):
        with Timer() as t:
            cy.factorial(100)
        results.append(t.secs)
    print(avg(results))


def avg(lst):
    tot_sum = 0
    for item in lst:
        tot_sum += item
    return tot_sum / len(lst)


if __name__ == '__main__':
    #if config.CONFIG['debug']:
    main()
