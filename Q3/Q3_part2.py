from os import close

def binary2int(binary): 
    int_val, i, n = 0, 0, 0
    while(binary != 0): 
        a = binary % 10
        int_val = int_val + a * pow(2, i) 
        binary = binary//10
        i += 1
    return int_val

# figuring out the length of the binary string.
f = open("Q3\Q3_input.txt", "r")

length = 0
oxygen = []
co2 = []

for x in f:
    x = x.split()
    length = len(x[0])
    oxygen.append(x[0])
    co2.append(x[0])

for i in range(0, len(oxygen[0])):
    zero_count = 0
    one_count = 0   
    for j in range(0, len(oxygen)):
        if (oxygen[j][i] == '0'):
            zero_count = zero_count + 1
        elif (oxygen[j][i] == '1'):
            one_count = one_count + 1
    if (zero_count > one_count):
        for k in range(0, len(oxygen)):
            if (oxygen[k][i] == '1'):
                oxygen[k] = '-1'
    elif ((one_count > zero_count) or (zero_count == one_count)):
        for k in range(0, len(oxygen)):
            if (oxygen[k][i] == '0'):
                oxygen[k] = '-1'
    while '-1' in oxygen:
        oxygen.remove('-1')
    if (len(oxygen) == 1):
        break

for i in range(0, len(co2[0])):
    zero_count = 0
    one_count = 0   
    for j in range(0, len(co2)):
        if (co2[j][i] == '0'):
            zero_count = zero_count + 1
        elif (co2[j][i] == '1'):
            one_count = one_count + 1
    if ((one_count > zero_count) or (zero_count == one_count)):
        for k in range(0, len(co2)):
            if (co2[k][i] == '1'):
                co2[k] = '-1'
    elif ((zero_count > one_count)):
        for k in range(0, len(co2)):
            if (co2[k][i] == '0'):
                co2[k] = '-1'
    while '-1' in co2:
        co2.remove('-1')
    if (len(co2) == 1):
        break
        

print(binary2int(int(oxygen[0])) * binary2int(int(co2[0])))