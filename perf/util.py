import random

def random_matrix(size, range_):
    mat = [[0]*size]*size # allocate 
    for i in range(size):
        for j in range(size):
            mat[i][j] = random.randint(0, range_)
    return mat 

