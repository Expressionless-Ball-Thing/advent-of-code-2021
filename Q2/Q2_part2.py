from os import close

f = open("Q2\Q2_input.txt", "r")
horizontal_pos = 0
depth = 0
aim = 0

for x in f:
    x = x.split()
    instruction = x[0]
    amount = int(x[1])
    if (instruction == "forward"):
        depth = depth + (aim * amount)
        horizontal_pos = horizontal_pos + amount
    elif (instruction == "down"):
        aim = aim + amount
    elif (instruction == "up"):
        aim = aim - amount

f.close()
print(horizontal_pos * depth)