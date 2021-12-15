class polymer:
    
    def __init__(self, rules, letters):
        self.rules = rules
        self.letters = letters
    
    # split the chain into boxes of two
    def insert_chain(self):
        insert_dict = {}
        for item in self.rules.keys():
            if self.rules[item][1] > 0:
                if self.rules[item][0] not in self.letters.keys():
                    self.letters[self.rules[item][0]] = self.rules[item][1]
                else:
                    self.letters[self.rules[item][0]] += self.rules[item][1]
                for new_item in self.rules[item][2]:
                    if new_item not in insert_dict.keys():
                        insert_dict[new_item] = self.rules[item][1]
                    else:
                        insert_dict[new_item] += self.rules[item][1]
                self.rules[item][1] = 0

        for item in insert_dict.keys():
            self.rules[item][1] += insert_dict[item]

    def iteration(self, steps):
        for i in range(0, steps):
            self.insert_chain()
    
    def count_chain(self):
        self.letters =dict(sorted(self.letters.items(),key= lambda x:x[1]))
        keys = list(self.letters.keys())
        return self.letters[keys[-1]] - self.letters[keys[0]]

f = open("Q14/Q14_input.txt", "r")
rules = {}

# turn the template into an array
template = [x for x in f.readline().strip()]
f.readline()
for x in f.readlines():
    x = x.strip().split(" -> ")
    rules[x[0]] = [x[1], 0, (str(x[0][0] + x[1]),  str(x[1] + x[0][1]))]

letters = {}
for letter in template:
    if letter not in letters.keys():
        letters[letter] = 1
    else:
        letters[letter] += 1

for index in range(0, len(template) - 1):
    key = template[index] + template[index + 1]
    rules[key][1] += 1

polymer_chain = polymer(rules, letters)
polymer_chain.iteration(10)
print("part 1:", polymer_chain.count_chain())
polymer_chain.iteration(30)
print("part 2:", polymer_chain.count_chain())