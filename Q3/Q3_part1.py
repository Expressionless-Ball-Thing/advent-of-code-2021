from os import close

def binary2int(binary): 
    result = 0
    length = len(binary)
    for i in range(0, length):
        result = result + (binary[i] * 2**(length - 1 - i))
    return result

# figuring out the length of the binary string.
f = open("Q3\Q3_input.txt", "r")

array = []

index = 0
gamma = []
epsilon = []

for x in f:
    x = x.split()
    length = len(x[0])
    array.append(x[0])
    index = index + 1   

print(len(array[0]))
for i in range(0, len(array[0])):
    zero_count = 0
    one_count = 0   
    for j in range(0, len(array)):
        if (array[j][i] == '0'):
            zero_count = zero_count + 1
        elif (array[j][i] == '1'):
            one_count = one_count + 1
    if (zero_count > one_count):
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

gamma_result = binary2int(gamma)
epsilon_result = binary2int(epsilon)

print(gamma_result*epsilon_result)
    
