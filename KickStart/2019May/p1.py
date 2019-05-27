import sys


T = int(sys.stdin.readline().strip())  # TEST number
# initializes, instructions = [], []
# for i in range(0, T+2, 2):
#     initialize = (list(map(int, sys.stdin.readline().strip().split(" "))))
#     initializes.append(initialize)
#     instruction = list(sys.stdin.readline().strip())
#     instructions.append(instruction)

for i in range(T):
    (N, R, C, Y, X) = (list(map(int, sys.stdin.readline().strip().split(" "))))
    instruction_round = list(sys.stdin.readline().strip())
    points_through = set()
    y, x = Y, X
    points_through.add((y, x))
    for instruction0 in instruction_round:
        if instruction0 == "N":
            y -= 1
            y_first = y
            while (y, x) in points_through:
                points_through.add((y, x))
                y -= 1
            points_through.add((y_first, x))
            points_through.add((y, x))

        elif instruction0 == "S":
            y += 1
            y_first = y
            while (y, x) in points_through:
                points_through.add((y, x))
                y += 1
            points_through.add((y, x))
            points_through.add((y_first, x))

        elif instruction0 == "W":
            x -= 1
            x_first = x
            while (y, x) in points_through:
                points_through.add((y, x))
                x -= 1
            points_through.add((y, x))
            points_through.add((y, x_first))
        else:
            x += 1
            x_first = x
            while (y, x) in points_through:
                points_through.add((y, x))
                x += 1
            points_through.add((y, x_first))
            points_through.add((y, x))
    print("Case #{}: {} {}".format(i+1, y, x))









