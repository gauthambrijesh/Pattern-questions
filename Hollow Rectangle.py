rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print(i+1, end=" ")
        else:
            print(" ", end=" ")
    print("")
