import numpy as np
import random

def dfs(list):
    pass

# easy shortest path search using nearest neighbour with numpy matrixes
# distances are mapped using square matrix A[i][j] represents distance between i and j
# order doesn't matter in case of distance between A and B
# distance is set randomly using random library
# path is mapped as a string that contains order of places being visited seperated by commas
def nn(list, index):
    list_len = len(list)
    unused_list = np.arange(0, len(list),1,int)
    path = str(index) + " -> "
    path_len = 0
    curr_index = index

    i = list_len
    while i > 1:
        unused_list = np.delete(unused_list, np.where(unused_list == curr_index))
        lowest_distance = np.nanmin(list[curr_index][unused_list])
        curr_index = int(np.where(list[curr_index] == lowest_distance)[0])
        path_len += lowest_distance
        path += str(curr_index)+" -> "
        i -= 1

    path += str(index)
    path_len += list[curr_index][index]
    return path, path_len

# version 1 of calculating mst
# will be using just classic looping through lists
# in future I will change it to use numpy built in functions
# it will also hold the graph of mst as a list

def mst(list):
    list_len = len(list)
    unused_list =  np.arange(0, list_len,1,int)
    used_list = np.array([])
    path = "0 - > "
    path_len = 0
    index = 0
    used_list = np.append(used_list, index)
    unused_list = np.delete(unused_list, np.where(unused_list == index))
    path_len += np.nanmin(list[index][unused_list])
    index = int(np.where(list[index] == path_len)[0])
    i = list_len
    while i > 1:
        unused_list = np.delete(unused_list, np.where(unused_list == index))
        lowest_distance = np.nan
        for x in used_list.astype(int):
            if np.isnan(lowest_distance):
                lowest_distance = np.nanmin(list[x][unused_list])
                next_index = int(np.where(np.nanmin(list[x][unused_list]) == lowest_distance)[0])
            else:
                if np.nanmin(list[x][unused_list]) < lowest_distance:
                    lowest_distance = np.nanmin(list[x][unused_list])
                    next_index = int(np.where(np.nanmin(list[x][unused_list]) == lowest_distance)[0])
        path_len += lowest_distance
        path += str(index)+ " -> " + str(next_index) + ","
        index = next_index
        used_list = np.append(used_list, index)
        i -= 1
    return used_list, len(used_list), list_len, path_len, path
    # return path, path_len

        


list = np.zeros((5,5))

for i in range(len(list)):
    for j in range(i,len(list[i])):
        if i == j:
            list[i][j] = np.nan
            continue
        rand = random.uniform(0,10)
        list[i][j] = rand
        list[j][i] = rand

print(list,"\n")
for x in range(len(list)):
    print(nn(list, x))

print(mst(list))


