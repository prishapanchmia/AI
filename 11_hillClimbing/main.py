def climb_one_step(mat, x, y):
    maxx = x
    maxy = y
    maxval = mat[x][y]
    if is_valid(mat, x+1, y):
        if mat[x+1][y] > maxval:
            maxx = x+1
            maxy = y
            maxval = mat[x+1][y]
    if is_valid(mat,x - 1, y):
        if mat[x - 1][y] > maxval:
            maxx = x - 1
            maxy = y
            maxval = mat[x - 1][y]
    if is_valid(mat,x, y+1):
        if mat[x][y+1] > maxval:
            maxx = x
            maxy = y + 1
            maxval = mat[x][y+1]
    if is_valid(mat, x, y-1):
        if mat[x][y-1] > maxval:
            maxx = x
            maxy = y - 1
            maxval = mat[x][y-1]
    # print("returning",maxx,maxy)
    return [maxx,maxy]


def is_valid(mat, x, y):
    rows = len(mat)
    cols = len(mat[0])
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= rows:
        return False
    if y >= cols:
        return False
    return True

n = int(input("Enter the size of the matrix: "))
mat = list()
for i in range(n):
    row_str = input().split()
    row = list()
    for string in row_str:
        row.append(int(string))
    mat.append(row)

x_start = int(input("Enter the starting x coordinate: "))
y_start = int(input("Enter the starting y coordinate: "))

for i in range(n):
    print(mat[i])

currx = x_start
curry = y_start
prevx = -1
prevy = -1
while True:
    next_step_cords = climb_one_step(mat, currx, curry)
    # print(next_step_cords)
    prevx = currx
    prevy = curry
    currx = next_step_cords[0]
    curry = next_step_cords[1]
    if currx == prevx and curry == prevy :
        print(f"Stabilized at {next_step_cords[0]}, {next_step_cords[1]} with value {mat[next_step_cords[0]][next_step_cords[1]]}")
        break
    else:
        print(f"Position is {next_step_cords[0]}, {next_step_cords[1]}" )
        continue