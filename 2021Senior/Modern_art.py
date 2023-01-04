# Calculate the number of gold spaces after K executions on a N x M grid

N = int(input())
M = int(input())
K = int(input())

row_t    =  N * [False]
column_t =  M * [False]

# Note the final state of the grid after all the transformations

for i in range(K):
    axes, no = input().split()
    if axes == "R":
        row_t[int(no) -1] = not row_t[int(no) - 1]
    else:
        column_t[int(no) - 1] = not column_t[int(no) - 1]


# Logic - 

r_weight = sum(row_t)
r_counter = N - r_weight

c_weight = sum(column_t)
c_counter = M - c_weight

gold_count = r_weight * c_counter + c_weight * r_counter
print(gold_count)

# Time complexity: O(x)