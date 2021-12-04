
# see if number is on the sheet, replace it with a -1
def number_in_sheet (bingo, num):
    for row in range(0,5):
        for col in range(0,5):
            if int(bingo[row][col]) == int(num):
                bingo[row][col] = -1

def calculate_final (bingo):
    final = 0
    for row in range(0,5):
        for col in range(0,5):   
            if (bingo[row][col] != -1):
                final = final + int(bingo[row][col])
    return final

def did_i_win (bingo):
    # row check
    for row in range(0,5):
        win = True
        for col in range(0,5):
            if (bingo[row][col] != -1):
                win = False
                break
        if (win == True):
            return True

    # column check
    for col in range(0,5):
        win = True
        for row in range(0,5):
            if (bingo[row][col] != -1):
                win = False
                break
        if (win == True):
            return True   


f = open("Q4\Q4_input.txt", "r")

bingo_list = []

num_list = f.readline().split("\n")
num_list = num_list[0].split(",")

print(f.readline())

# Load the bingo sheets into a 2d array.
index = 0
board_counter = 0
temp = []

for x in f:
    if board_counter < 4:
        x = x.split("\n")
        temp.append(x[0].split())
        board_counter = board_counter + 1
    elif board_counter == 4:
        x = x.split("\n")
        temp.append(x[0].split())
        bingo_list.append(temp)
        temp = []
        board_counter = board_counter + 1
    else:
        board_counter = 0

lowest_to_win = 0
final_score = 0

for bingo in bingo_list:
    # check if a number is in the bingo sheet
    num_count = 1
    for number in num_list:
        number_in_sheet(bingo, number)
        # check if we hit a row, or column
        if (did_i_win(bingo) == True):
            if lowest_to_win == 0 or lowest_to_win <= num_count:
                lowest_to_win = num_count
                final_score = calculate_final(bingo) * int(number)
            break
        num_count = num_count + 1

print(lowest_to_win)
print(final_score)