hex_conversion  = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

string = ""

f = open("Q16/Q16_input.txt")
x = f.readline().strip()

for character in x:
    string += hex_conversion[character]

print(string)
total_version = 0

counter = 0
while counter < len(string):
    #get version number
    #print("version", int((string[counter : counter + 3]), 2))
    total_version += int((string[counter : counter + 3]), 2)
    counter += 3

    ID = int((string[counter : counter + 3]), 2)
    counter += 3
    #print("ID", ID)
    
    if ID == 4:
        while True:
            # reading the packet
            #print(string[counter : counter + 5]," ", int(string[counter + 1 : counter + 5],2))
            if int(string[counter],2) == 1:
                counter += 5
            elif int(string[counter], 2) == 0:
                counter += 5
                break
    else:
        if int(string[counter],2) == 1:
            #print(string[counter : counter + 12]," ", int(string[counter + 1 : counter + 12],2))
            counter += 12
        elif int(string[counter],2) == 0:
            #print(string[counter : counter + 16]," ", int(string[counter + 1 : counter + 16],2))
            counter += 16            

    if string[counter:] == "" or int(string[counter:], 2) == 0:
        break

print("total version", total_version)