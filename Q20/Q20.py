
class trench:
    def __init__(self, algo, trench_map) -> None:
        self.algo = algo
        self.trench_map = trench_map
        self.row, self.col = len(trench_map), len(trench_map[0])
        self.copy = {} # copy so we can replace it later.
        self.infinite = "0"
        self.realSize = self.row
    def __repr__(self):
        for x in self.trench_map:
            print("".join(x))
        return ""

    def get_surrounding_pixels (self, row, col):
        result = []
        table = [(row-1, col-1),(row-1, col),(row-1, col+1),(row,col-1),(row,col),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]
        for coord in table:
            if (coord[0] >= 0 and coord[1] >= 0 and coord[0] < self.row and coord[1] < self.col):
                result.append(self.trench_map[coord[0]][coord[1]])
            else:
                result.append(str(self.infinite))
        #print({row}, {col}, result, int("".join(result),2))
        return int("".join(result),2)
    
    def get_new_pixels (self):
        self.increase_size()
        self.row += 2
        self.col += 2
        for row in range(0, self.row):
            for col in range(0, self.col):
                self.copy[(row, col)] = self.algo[self.get_surrounding_pixels(row,col)]
        for coord in self.copy.keys():
            self.trench_map[coord[0]][coord[1]] = self.copy[coord]
        self.copy = {}
        if self.infinite == "0":
            self.infinite = "1"
        else:
            self.infinite = "0"

    def count_lit_pixels(self):
        count = 0
        for row in range(0, self.row):
            for col in range(0, self.col):
                if self.trench_map[row][col] == "1":
                    count += 1
        print(count)

    def increase_size(self):
        #appending existing rows
        for row in range(0,self.row):
            self.trench_map[row] = [self.infinite] + self.trench_map[row] + [self.infinite]
        #adding the new rows on the top and bottom
        self.trench_map = [[ str(self.infinite) for _ in range(self.row + 2) ]] + self.trench_map + [[ str(self.infinite) for _ in range(self.row + 2) ]]
    
    def enhance(self, count):
        for _ in range(count):
            self.get_new_pixels()


f = open("Q20/Q20_input.txt", "r")

algo = f.readline().strip().replace("#", "1").replace(".", "0")
trench_map = []
f.readline() # skip a line
for x in f.readlines():
    trench_map.append([character for character in x.strip().replace("#", "1").replace(".", "0")])
new_trench = trench(algo, trench_map)

new_trench.enhance(2)

print("part 1: ", end="")
new_trench.count_lit_pixels()

new_trench.enhance(48)

print("part 2: ", end="")
new_trench.count_lit_pixels()
