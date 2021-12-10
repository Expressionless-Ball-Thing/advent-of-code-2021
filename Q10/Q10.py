from os import error


class Stack:
    def __init__(self):
        self.stack = []
        self.middle_score_list = []

    def push_stack(self, bracket):
        self.stack.append(bracket)

    def pop_stack(self):
        return self.stack.pop(-1)

    def stack_clear(self):
        self.stack = []

    def find_opposite(self):
        self.middle_score = 0
        if(len(self.stack) == 0):
            return
        for opening in range(len(self.stack)-1, -1, -1):
            if (self.stack[opening] == "("):
                self.middle_score = self.middle_score * 5 + 1
            elif (self.stack[opening] == "["):
                self.middle_score = self.middle_score * 5 + 2
            elif (self.stack[opening] == "{"):
                self.middle_score = self.middle_score * 5 + 3
            else:
                self.middle_score = self.middle_score * 5 + 4
        self.middle_score_list.append(self.middle_score)
    
    def middle(self):
        self.middle_score_list.sort()
        return self.middle_score_list[int((len(self.middle_score_list) - 1) / 2)]

f = open("Q10/Q10_input.txt")

error_score = 0
middle_score = 0

New_stack = Stack()

points_dict = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

opposite_bracket = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<" 
}

for x in f:
    x = (x.split("\n"))[0]

    for bracket in x:
        if bracket in ["[", "(", "<", "{"]:
            New_stack.push_stack(bracket)
        else:
            if (New_stack.pop_stack() != opposite_bracket[bracket]):
                error_score += points_dict[bracket]
                New_stack.stack_clear()
                break
    New_stack.find_opposite()
    New_stack.stack_clear()

print("syntax error score:",error_score)
print("middle score:", New_stack.middle())
