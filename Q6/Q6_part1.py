class Lanternfish_spawn:
    def __init__(self, initial_state):
        self.state = initial_state
    
    def progress_day(self):
        start = 0
        end = len(self.state)
        for index in range(start, end):
            if (self.state[index] == 0):
                self.state[index] = 6
                self.state.append(8)
            else:
                self.state[index] = self.state[index] - 1
    
    def days_passed(self, days):
        for i in range(0, days):
            self.progress_day()
    
    def fish_count(self):
        return len(self.state)
                

f = open("Q6/Q6_input.txt", "r")

initial_state = f.readline().split(",")
f.close()
initial_state = [int(el) for el in initial_state]
big_spawn = Lanternfish_spawn(initial_state)
big_spawn.days_passed(80)
print(big_spawn.fish_count())

