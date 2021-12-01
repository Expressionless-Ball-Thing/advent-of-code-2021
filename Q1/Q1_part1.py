
f = open("Q1\Q1_input.txt", "r")

current = 0
increase_count = -1

for x in f:
    x = int(x)
    if x > current:
        increase_count = increase_count + 1 
    current = x

print(increase_count)


