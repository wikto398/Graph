import os
import numpy as np
import random

def dfs(list):
    pass

def nn(list, index):
    used_list = np.zeros(len(list))
    paths = []
    curr_path = [[],[]]
    

list = np.zeros((7,7))

for i in range(len(list)):
    for j in range(len(list[i])):
        if i == j:
            continue
        if i > j:
            continue
        list[i][j] = random.uniform(0,10)


print(list)

