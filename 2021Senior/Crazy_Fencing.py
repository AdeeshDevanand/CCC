# calculates the area of N fences

N = int(input())
h_inp = input().split() # list of N + 1 heights
lol = map(int, h_inp[:])
lor = map(int, h_inp[1:])
low = map(int, input().split())  # list of N widths
a_sum = 0

for left, width, right in zip(lol, low, lor):
    a_sum += width * ((left + right)/2)

print(a_sum)

'''
# Another solution

n = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))
area = 0

for i in range(n):
    left = heights[i]
    right = heights[i+1]
    width = widths[i]
    area += width * ((left + right)/2)

print(area)'''

# Time complexity - O(N)