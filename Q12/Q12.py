def find_path(current_pos, small_caves_accessed, small_caves_accessed_twice):
    path_count = 0
    path_count_2 = 0
    for path in cave_system:
        if path[0] == current_pos:
            if path[1] == 'end':
                path_count_2 += 1
                if (small_caves_accessed_twice == False):
                    path_count += 1
            elif path[1].islower() == True:
                if (path[1] in small_caves_accessed):
                    if (small_caves_accessed_twice == False and path[1] != 'start'):
                        result = find_path(path[1], small_caves_accessed, True)
                        path_count += result[0]
                        path_count_2 += result[1]
                else:
                    result = find_path(path[1], small_caves_accessed + [path[1]], small_caves_accessed_twice)
                    path_count += result[0]
                    path_count_2 += result[1]                   
            else:
                result = find_path(path[1], small_caves_accessed, small_caves_accessed_twice)
                path_count += result[0]
                path_count_2 +=  result[1] 
        elif path[1] == current_pos:
            if path[0] == 'end':
                path_count_2 += 1
                if (small_caves_accessed_twice == False):
                    path_count += 1
            elif path[0].islower() == True:
                if (path[0] in small_caves_accessed):
                    if (small_caves_accessed_twice == False and path[0] != 'start'):
                        result = find_path(path[0], small_caves_accessed, True)
                        path_count += result[0]
                        path_count_2 += result[1]
                else:
                    result = find_path(path[0], small_caves_accessed + [path[0]], small_caves_accessed_twice)
                    path_count += result[0]
                    path_count_2 += result[1]    
            else:
                result = find_path(path[0], small_caves_accessed, small_caves_accessed_twice)
                path_count += result[0]
                path_count_2 += result[1] 
    return [path_count, path_count_2]       
f = open("Q12/Q12_input.txt", "r")

cave_system = [i.strip() for i in f.readlines() if i.strip() != ""]
cave_system = [tuple(x.split("-")) for x in cave_system]


print(find_path('start', ['start'], False))