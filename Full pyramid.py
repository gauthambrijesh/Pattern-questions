rows = 5
n = 2 * rows - 2
for i in range(0, rows+1):
    for j in range(0, n+1):
        print(end=" ")
    n = n - 1
    for j in range(0, i):
        print(i, end=" ")
    print("")