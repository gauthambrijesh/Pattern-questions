rows = 5
n = 2 * rows - 2
for i in range(rows, 0, -1):
    for j in range(n, 0, -1):
        print(end=" ")
    n = n + 1
    for j in range(0, i):
        print(i, end=" ")
    print("")