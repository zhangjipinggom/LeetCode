import sys

T = int(sys.stdin.readline().strip())  # TEST number
for i in range(T):
    (R, C, K) = (list(map(int, sys.stdin.readline().strip().split(" "))))
    max_square = 1
    if C == 1:
        print("Case #{}: {}".format(i + 1, R))
        break
    if R == 1:
        row_v = (list(map(int, sys.stdin.readline().strip().split(" "))))
        max_neighbour = []
        max_neighbour0 = 1
        for j in range(1, C, 1):
            if row_v[j] - row_v[j-1] <= K:
                max_neighbour0 += 1
            else:
                max_neighbour.append(max_neighbour0)
                max_neighbour0 = 1
            max_neighbour.append(max_neighbour0)
            max_neighbour_sort = sorted(max_neighbour)
            max_square = max_neighbour_sort[-1]
        print("Case #{}: {}".format(i + 1, max_square))
        break
    for r0 in range(R):
        row_v = (list(map(int, sys.stdin.readline().strip().split(" "))))
        row_v2 = row_v.copy()
        row_v2.pop(0)
        row_difference = list(map(lambda x: max(x[0] - x[1], x[1] - x[0]), zip(row_v[:-1], row_v2)))
        for row_difference0 in row_difference:
            if row_difference <= K:
                max_square += 1
        if max(row_v[-1] - row_v[-2], row_v[-2], row_v[-1]) <= K:
            max_square += 1
    print("Case #{}: {}".format(i+1, max_square))









