# [10,1,2,3,4,5,6,7,8,9]

class game:

    def __init__(self, starting_pos):
        self.current_pos = starting_pos
        self.score = [0 ,0]
        self.roll_count = 0
        self.die = [1,2,3]
    
    def __repr__(self):
        print("current positions", self.current_pos)
        print("score", self.score)
        print("roll", self.roll_count)
        print("die", self.die)
        return ""
    
    def roll(self):
        
        while True:
            for player in range(0,len(self.current_pos)):
                position = self.current_pos[player]
                for die in self.die:
                    position += die
                self.new_score_position(position, player)
                self.die = self.increment_die(self.die)
                if self.score[player] >= 1000:
                    return

    def new_score_position(self, position, player_num):
        if position > 10:
            position %= 10
            if position == 0:
                position = 10
        
        self.score[player_num] += position
        self.current_pos[player_num] = position


    def increment_die (self, die):
        die = [x + 3 for x in die]
        for index in range(len(die)):
            if die[index] > 100:
                die[index] = die[index] % 100
        self.roll_count += 3
        return die
    
    def loser_score (self):
        self.score.sort()
        return self.score[0] * self.roll_count


f = open("Q21/Q21_input.txt", "r")

starting_pos = []
for x in f.readlines():
    starting_pos.append(int(x.strip()[-1]))
new_game = game(starting_pos)

new_game.roll()
print(new_game)
print(new_game.loser_score())
