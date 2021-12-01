
f = open("Q1\Q1_input.txt", "r")

current = 0
increase_count = -1

A = -1
B = -1
C = -1
sum = 0

for x in f:
    if A == -1:
        A = int(x)
    elif B == -1:
        B = int(x)
    elif C == -1:
        C = int(x)
        sum = A + B + C
        if sum > current:
            increase_count = increase_count + 1 
        current = sum
        A = B
        B = C
        C = -1

print(increase_count)


