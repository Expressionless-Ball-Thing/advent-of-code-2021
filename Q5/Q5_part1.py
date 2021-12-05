f = open("Q5\Q5_input.txt", "r")
vent_dict = {}

def in_line(coord1, coord2):

    # see if their x coords or y coords match
    # if the x coord match
    if (coord1[0] == coord2[0]):
        # count upwards
        if (coord1[1] < coord2[1]):
            for y in range(int(coord1[1]), int(coord2[1]) + 1):
                new_coord = (coord1[0], y)
                if new_coord not in vent_dict.keys():
                    vent_dict[new_coord] = 1
                else:
                    vent_dict[new_coord] = vent_dict[new_coord] + 1
        # count downards
        elif (coord1[1] > coord2[1]):
            for y in range(int(coord1[1]), int(coord2[1]) - 1, -1):
                new_coord = (int(coord1[0]), y)
                if new_coord not in vent_dict.keys():
                    vent_dict[new_coord] = 1
                else:
                    vent_dict[new_coord] = vent_dict[new_coord] + 1  
    elif (coord1[1] == coord2[1]):
        # go to the right
        if (coord1[0] < coord2[0]):
            for k in range(int(coord1[0]), int(coord2[0]) + 1):
                new_coord = (k, int(coord1[1]))
                if new_coord not in vent_dict.keys():
                    vent_dict[new_coord] = 1
                else:
                    vent_dict[new_coord] = vent_dict[new_coord] + 1
        # count downards
        elif (coord1[0] > coord2[0]):
            for k in range(int(coord1[0]), int(coord2[0]) - 1, -1):
                new_coord = (k, int(coord1[1]))
                if new_coord not in vent_dict.keys():
                    vent_dict[new_coord] = 1
                else:
                    vent_dict[new_coord] = vent_dict[new_coord] + 1  

# loadage
for line in f:
    line = line.split("\n")[0].split(" -> ")
    coord1array = line[0].split(",")
    coord2array = line[1].split(",")
    coord1 = (int(coord1array[0]), int(coord1array[1]))
    coord2 = (int(coord2array[0]), int(coord2array[1]))
    in_line(coord1, coord2)

overlap_count = 0
for count in vent_dict.values():
    if (count >= 2):
        overlap_count = overlap_count + 1
print(overlap_count)