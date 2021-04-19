import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json


def read_file(file="./results.json"):
    data = {}
    with open(file) as json_file:
        data = json.load(json_file)
    return data


data = read_file()
for tst, D in data.items():
    plt.bar(*zip(*D.items()))
    plt.savefig(f"./graph/img/{tst}.png")
