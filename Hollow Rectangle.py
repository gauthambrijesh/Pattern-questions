rows = 6
cols = 6
for i in range(1,rows):
    for j in range(1,cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print("")
