import random

def random_matrix(size, range_):
    mat = [[0]*size]*size # allocate 
    for i in range(size):
        for j in range(size):
            mat[i][j] = random.randint(0, range_)
    return mat 



class result:
    def __init__(self, name, pypy_res, cy_res):
        self.name = name 
        self.pypy_res = pypy_res
        self.py_avg = self.avg(self.pypy_res)
        self.cy_res = cy_res
        self.cy_avg = self.avg(self.cy_res)
        

    def display(self):
        print(f"{self.name} test PYPY:{self.py_avg}")
        print(f"{self.name} test Cy  :{self.cy_avg}")
        print(f"A difference of {round(self.py_avg/self.cy_avg, 4)}x in performance")
        print("\n")

    
    def avg(self, lst):
        tot_sum = 0
        for item in lst:
            tot_sum += item
        return tot_sum / len(lst)
