from queue import Queue
from collections import defaultdict

## Part 1
## Logic - Arbitrarity tree, Genrec
##       - Generate the different nodes for each minute and traverse using BFS
##       - Implemented using a station_wl and time_wl working in tandem
##       - NEED TO IMPLEMENT VISITED

N, W, D = map(int, input().split()) # N stations, W pathways, D days
adjacency_lst = defaultdict(list)


## create pathways between stations
for i in range(W):
    fr, to = input().split()
    adjacency_lst[fr].append(to)

subway = list(input().split())
## Termination arguement
##
##
def solve(subway, station_wl, time_wl):
    while not station_wl.empty():

        curr_st = station_wl.get()
        curr_time = time_wl.get()

        if curr_st == str(N):
            print(curr_time)
            break

        else:
            for walkway in adjacency_lst[curr_st]:
                station_wl.put(walkway)     # adding curr station's pathways
                time_wl.put(curr_time + 1)  # adding corresponding times

            if curr_time + 1 < N:           # catches list index out of range error
                station_wl.put(subway[curr_time + 1]) # adding train's pathway
                time_wl.put(curr_time + 1)            # adding train's time


# [1, 9, 7, 2, 5, 8, 6, 3, 4, 10]

## Part 2 
for i in range(D):
    ind1, ind2 = map(lambda x : int(x) - 1, input().split())
    subway[ind1], subway[ind2] = subway[ind2], subway[ind1]
    station_wl = Queue()
    time_wl = Queue()
    station_wl.put("1")
    time_wl.put(0)
    solve(subway, station_wl, time_wl)