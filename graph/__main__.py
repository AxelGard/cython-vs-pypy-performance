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
for tst, res in data.items():
    plt.bar(np.array(list(res.keys())), np.array(list(res.values())))
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.savefig(f"./graph/img/{tst}.png")
