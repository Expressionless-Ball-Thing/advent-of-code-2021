class polymer:
    
    def __init__(self, template, rules):
        self.chain = template
        self.rules = rules
        self.count = {}
    
    # split the chain into boxes of two
    def insert_chain(self):

        # figuring out the elements to insert
        insert = []
        for index in range(0, len(self.chain) - 1):
            key = self.chain[index] + self.chain[index + 1]
            insert.append(self.rules[key])
        insert.append(0)

        # combining the chain and the insert together.
        new_chain = []
        for i in range(0, len(self.chain)):
            new_chain.append(self.chain[i])
            new_chain.append(insert[i])
        new_chain.pop()
        self.chain = new_chain
    
    def iteration(self, steps):
        for i in range(0, steps):
            self.insert_chain()
    
    def count_chain(self):
        for item in self.chain:
            if item not in self.count.keys():
                self.count[item] = 1
            else:
                self.count[item] += 1
        self.count =dict(sorted(self.count.items(),key= lambda x:x[1]))
        print(self.count)
        keys = list(self.count.keys())
        print("part 1:", self.count[keys[-1]] - self.count[keys[0]])

f = open("Q14/Q14_input.txt", "r")
rules = {}

# turn the template into an array
template = [x for x in f.readline().strip()]
f.readline()
for x in f.readlines():
    x = x.strip().split(" -> ")
    rules[x[0]] = x[1]

polymer_chain = polymer(template, rules)
polymer_chain.iteration(10)
polymer_chain.count_chain()