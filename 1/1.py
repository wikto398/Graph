import numpy as np
import random

def dfs(list):
    pass

# version 2
# easy shortest path search using nearest neighbour with numpy matrixes
# distances are mapped using square matrix A[i][j] that represents distance between i and j
# order doesn't matter in case of distance between A and B
# distance is set randomly using random library
# path is mapped as a string that contains order of places being visited seperated by arrows for clearer view
# update 1 function counts all nn paths and return shortest path(s) and the distance, instead of counting and returning paths separetely

def nn(list):
    list_len = len(list)
    path_len = np.zeros(list_len)
    paths = np.array([])
    for index in range(list_len):
        unused_list = np.arange(0, len(list),1,int)
        path = str(index) + " -> " 
        curr_index = index

        while len(unused_list) > 1:
            unused_list = np.delete(unused_list, np.where(unused_list == curr_index))
            lowest_distance = np.nanmin(list[curr_index][unused_list])
            curr_index = int(np.where(list[curr_index] == lowest_distance)[0])
            path_len[index] += lowest_distance
            path += str(curr_index)+" -> "

        path += str(index)
        paths = np.append(paths, path)
        path_len[index] += list[curr_index][index]
    min = np.nanmin(path_len)
    min_path = str(paths[np.where(path_len == min)])
    return min_path, min

# version 1 of calculating mst
# function creates path how graph expands from starting vertex
# function calculates the distance of the tree
# it returns path and distance
# might do some speed updates in future if answers come to mind

def mst(list):
    list_len = len(list)
    unused_list =  np.arange(0, list_len,1,int)
    used_list = np.array([])
    path = ""
    path_len = 0
    index = 0
    used_list = np.append(used_list, index)
    while len(used_list) < list_len:
        unused_list = np.delete(unused_list, np.where(unused_list == index))
        lowest_distance = 0
        for x in used_list.astype(int):
            distance = np.nanmin(list[x][unused_list])
            if lowest_distance != 0:
                if distance < lowest_distance:
                    lowest_distance = distance
                    index_next = int(np.where(list[x] == lowest_distance)[0])
                    index = x
            else:
                lowest_distance = distance
                index_next = int(np.where(list[x] == lowest_distance)[0])
                index = x
        path_len += lowest_distance
        path += str(index) + " - > " + str(index_next) + ", "
        index = index_next
        used_list = np.append(used_list, index)
    return path, path_len, 

        
file = open("matrix.txt", "w")

list = np.zeros((10,10))

for i in range(len(list)):
    for j in range(i,len(list[i])):
        if i == j:
            list[i][j] = np.nan
            continue
        rand = random.uniform(5,10)
        list[i][j] = rand
        list[j][i] = rand

print(list,"\n")

file.write(str(list))

print(nn(list))
print(mst(list))

nn_distance = nn(list)[1]
mst_distance = mst(list)[1]
print(nn_distance/mst_distance*100,"%")






