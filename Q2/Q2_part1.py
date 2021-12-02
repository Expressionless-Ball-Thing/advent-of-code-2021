from os import close

f = open("Q2\Q2_input.txt", "r")
horizontal_pos = 0
depth = 0

for x in f:
    x = x.split()
    instruction = x[:-3]
    amount = int(x[-2:])
    if (instruction == "forward"):
        horizontal_pos = horizontal_pos + amount
    elif (instruction == "down"):
        depth = depth + amount
    elif (instruction == "up"):
        depth = depth - amount
        
f.close()
print(horizontal_pos * depth)