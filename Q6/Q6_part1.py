class Lanternfish_spawn:
    def __init__(self, initial_state):
        self.state = initial_state
        self.new_fish_batch = []
        self.initial_length = len(initial_state)
    
    
    def progress_day(self):
        start = 0
        end = len(self.state)
        new_fish_count = 0
        # going over the initial fish
        for index in range(start, self.initial_length):
            if (self.state[index] == 0):
                self.state[index] = 6
                new_fish_count = new_fish_count + 1
            else:
                self.state[index] = self.state[index] - 1
        # going over the new_fish_batch
        for index in range(start, len(self.new_fish_batch)):
            if (self.new_fish_batch[index][1] == 0):
                self.new_fish_batch[index][1] = 6
                new_fish_count = new_fish_count + self.new_fish_batch[index][0]
            else:
                self.new_fish_batch[index][1] = self.new_fish_batch[index][1] - 1
        if (new_fish_count != 0):
            self.new_fish_batch.append([new_fish_count, 8])

    
    def days_passed(self, days):
        for i in range(0, days):
            self.progress_day()
    
    def fish_count(self):
        return len(self.state) + sum([x[0] for x in self.new_fish_batch])
                

f = open("Q6/Q6_input.txt", "r")

initial_state = f.readline().split(",")
f.close()
initial_state = [int(el) for el in initial_state]
big_spawn = Lanternfish_spawn(initial_state)
big_spawn.days_passed(256)
print(big_spawn.fish_count())

