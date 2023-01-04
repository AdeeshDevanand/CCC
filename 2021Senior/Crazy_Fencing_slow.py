## calculates the area of N andjacent fences
## uses recursion (python has a recursion limit)

def main():
    n, loh, low = get_input()
    l = loh.pop(0)
    print(solve(l, loh, low, 0))
    return

def get_input():
    n = int(input())
    loh = list(map(int, input().split()))  # list of N + 1 heights
    low = list(map(int, input().split()))  # list of N widths
    return n, loh, low

def solve(l, loh, low, area):
    if not loh:
        return area
    else:
        w = low.pop(0)
        r = loh.pop(0)
        area += calc_area(l, w, r)
        return solve(r, loh, low, area)

def calc_area(l, w, r):
    return w * ((l + r)/2)

main()