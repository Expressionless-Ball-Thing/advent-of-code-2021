f = open("Q5\Q5_input.txt", "r")
vent_dict = {}

def is_vertical(coord1, coord2):

    # see if their x coords or y coords match
    # if the x coord match
        # count upwards
    if (coord1[1] < coord2[1]):
        for y in range(coord1[1], coord2[1] + 1):
            new_coord = (coord1[0], y)
            if new_coord not in vent_dict.keys():
                vent_dict[new_coord] = 1
            else:
                vent_dict[new_coord] = vent_dict[new_coord] + 1
    # count downards
    elif (coord1[1] > coord2[1]):
        for y in range(coord1[1], coord2[1] - 1, -1):
            new_coord = (coord1[0], y)
            if new_coord not in vent_dict.keys():
                vent_dict[new_coord] = 1
            else:
                vent_dict[new_coord] = vent_dict[new_coord] + 1  

def is_horizontal(coord1, coord2):
    if (coord1[0] < coord2[0]):
        for k in range(coord1[0], coord2[0] + 1):
            new_coord = (k, coord1[1])
            if new_coord not in vent_dict.keys():
                vent_dict[new_coord] = 1
            else:
                vent_dict[new_coord] = vent_dict[new_coord] + 1
        # count downards
    elif (coord1[0] > coord2[0]):
        for k in range(coord1[0], coord2[0] - 1, -1):
            new_coord = (k, int(coord1[1]))
            if new_coord not in vent_dict.keys():
                vent_dict[new_coord] = 1
            else:
                vent_dict[new_coord] = vent_dict[new_coord] + 1      

# test to see if the points can be joined by drawing a line of gradient 1 or -1.
def diagonal_test(coord1, coord2):
    if ((coord2[1] - coord1[1]) / (coord2[0] - coord1[0]) == 1 or -1):
        if (coord2[1] > coord1[1] and coord2[0] > coord1[0]):
            return (1, 1)
        elif (coord2[1] > coord1[1] and coord2[0] < coord1[0]):
            return (-1, 1)
        elif (coord2[1] < coord1[1] and coord2[0] < coord1[0]):
            return (-1, -1)
        else:
            return (1, -1)
    return False

# fill in the diagonal coordinates
def is_diagonal(coord1, coord2, step):
    while (coord1 != coord2):
        if coord1 not in vent_dict.keys():
            vent_dict[coord1] = 1
        else:
            vent_dict[coord1] = vent_dict[coord1] + 1  
        coord1 = (coord1[0] + step[0], coord1[1] + step[1])
    if coord2 not in vent_dict.keys():
        vent_dict[coord2] = 1
    else:
        vent_dict[coord2] = vent_dict[coord2] + 1            

# loadage
for line in f:
    line = line.split("\n")[0].split(" -> ")
    coord1array = line[0].split(",")
    coord2array = line[1].split(",")
    coord1 = (int(coord1array[0]), int(coord1array[1]))
    coord2 = (int(coord2array[0]), int(coord2array[1]))
    if (coord1[0] == coord2[0]):
        is_vertical(coord1, coord2)
    elif (coord1[1] == coord2[1]):
        is_horizontal(coord1, coord2)
    else:
        thing = diagonal_test(coord1, coord2)
        if (thing):
            is_diagonal(coord1, coord2, thing)

overlap_count = 0
for count in vent_dict.values():
    if (count >= 2):
        overlap_count = overlap_count + 1
print(overlap_count)