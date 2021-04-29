import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json


def read_file(file="./results.json"):
    data = {}
    with open(file) as json_file:
        data = json.load(json_file)
    return data

def add_labels(x,y):
    for i in range(len(x)):
        plt.text(i,round(y[i], 7), round(y[i], 7))


data = read_file()
for tst, res in data.items():
    plt.figure()
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.bar(np.array(list(res.keys())), np.array(list(res.values())))
    add_labels(list(res.keys()), list(res.values()))
    plt.savefig(f"./graph/img/{tst}.png")
