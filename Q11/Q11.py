def light_up(grid):
    light_up_count = 0
    all_light = True
    for row in range(0, len(grid)):
        for col in range(0, len(grid)):
            grid[row][col] += 1

    for row in range(0, len(grid)):
        for col in range(0, len(grid)):
            if (grid[row][col] > 9):
                grid[row][col] = 0
                light_adjacent(grid, row, col)


    for row in range(0, len(grid)):
        for col in range(0, len(grid)):
            if (grid[row][col] == 0):  
                light_up_count = light_up_count + 1
            else:
                all_light = False
                
    return [light_up_count, all_light]

def light_adjacent(grid, row, col):
    height, width = len(grid) - 1, len(grid) - 1
    # increase the adjacent octopuses one by one.

    if (row != 0 and col != 0 and grid[row - 1][col - 1] != 0):
        grid[row - 1][col - 1] += 1
        if (grid[row - 1][col - 1] > 9):
            grid[row - 1][col - 1] = 0
            light_adjacent(grid, row - 1, col - 1)

    if (row != 0 and grid[row - 1][col] != 0):
        grid[row - 1][col] += 1
        if (grid[row - 1][col] > 9):
            grid[row - 1][col] = 0
            light_adjacent(grid, row - 1, col)       

    if (row != 0 and col != width and grid[row - 1][col + 1] != 0):
        grid[row - 1][col + 1] += 1 
        if (grid[row - 1][col + 1] > 9):
            grid[row - 1][col + 1] = 0
            light_adjacent(grid, row - 1, col + 1) 

    if (col != 0 and grid[row][col - 1] != 0):
        grid[row][col - 1] += 1
        if (grid[row][col - 1] > 9):
            grid[row][col - 1] = 0
            light_adjacent(grid, row, col - 1)

    if (col != width and grid[row][col + 1] != 0):
        grid[row][col + 1] += 1
        if (grid[row][col + 1] > 9):
            grid[row][col + 1] = 0
            light_adjacent(grid, row, col + 1)

    if (row != height and col != 0 and grid[row + 1][col - 1] != 0):
        grid[row + 1][col - 1] += 1    
        if (grid[row + 1][col - 1] > 9):
            grid[row + 1][col - 1] = 0
            light_adjacent(grid, row + 1, col - 1)

    if (row != height and grid[row + 1][col] != 0):
        grid[row + 1][col] += 1
        if (grid[row + 1][col] > 9):
            grid[row + 1][col] = 0
            light_adjacent(grid, row + 1, col)

    if (row != height and col != width and grid[row + 1][col + 1] != 0):
        grid[row + 1][col + 1] += 1
        if (grid[row + 1][col + 1] > 9):
            grid[row + 1][col + 1] = 0
            light_adjacent(grid, row + 1, col + 1)

f = open("Q11/Q11_input.txt", "r")


grid = [i.strip() for i in f.readlines() if i.strip() != ""]
grid = [[int(x) for x in line] for line in grid]

sum = 0
counter = 1
skip = False

while counter <= 100:
    result = light_up(grid)
    sum += result[0]
    if (result[1] == True and skip == False):
        print(counter)
        skip = True
    counter = counter + 1

print("total flashes after 100 steps:",sum)

while True:
    result = light_up(grid)
    if (result[1] == True):
        print("sync at step", counter)
        break
    counter = counter + 1