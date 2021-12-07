f = open("Q7/Q7_input.txt", "r")

crab_line = [int(x) for x in f.readline().split(",")]
crab_line.sort()

min = crab_line[0]
max = crab_line[-1]
lowest_fuel_part1 = -1
lowest_fuel_part2 = -1

for i in range(min, max + 1):
    fuel_count_part1 = 0
    fuel_count_part2 = 0
    for j in crab_line:
        fuel_count_part2 = fuel_count_part2 + ((abs(j-i) + 1)*(abs(j-i))/2)
        fuel_count_part1 = fuel_count_part1 + abs(j-i)
    if (lowest_fuel_part1 == -1 or lowest_fuel_part1 > fuel_count_part1):
        lowest_fuel_part1 = fuel_count_part1    
    if (lowest_fuel_part2 == -1 or lowest_fuel_part2 > fuel_count_part2):
        lowest_fuel_part2 = fuel_count_part2

print("part1: ", lowest_fuel_part1)
print("part2: ", lowest_fuel_part2)

