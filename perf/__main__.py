from . import config
from . import util
from . import tests



__version__ = "0.1.0"



def main():
    fac_res = tests.factorial_test()
    fac_res.display()

    mat_res = tests.matrix_multi_test()
    mat_res.display()

    add_num = tests.adding_numbers_test()
    add_num.display()



if __name__ == '__main__':
    if config.CONFIG['debug']:
        pass
    main()
