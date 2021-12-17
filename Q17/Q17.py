import math

def find_minx(left_end):
    minx = 1
    min_horizontal_range = 0
    while True:
        min_horizontal_range += minx
        if min_horizontal_range >= left_end:
            return minx
        else:
            minx += 1

def decreaseMagnitute(n):
    if n > 0:
        return n - 1
    elif n < 0:
        return n + 1
    else:
        return n

class ProbeTrajectorySolver:
    # Find and seperate the target bounds.
    def __init__(self, targetarea) -> None:
        target_x, target_y = targetarea[13:].split(", ")
        target_x = target_x[2:].split("..")
        target_y = target_y[2:].split("..")
        self.left_end = int(target_x[0])
        self.right_end = int(target_x[1])
        self.bottom_end = int(target_y[0])
        self.top_end = int(target_y[1])
        self.calculatedTrajectories = []

    def get_initial_velocity(self):
        # find the minimum horizontal velocity.
        minx = find_minx(self.left_end)
        # since any positive y will touch 0 again, test up to abs(self.bottom_end), since after that itll skip entirely
        for y in range(self.bottom_end, abs(self.bottom_end) + 1):
            for x in range(minx, self.right_end + 1):  # test for all x values
                if self.test_initial_velocity(x, y)[0]:
                    self.calculatedTrajectories.append((x, y))
        return self.calculatedTrajectories

    # see if the inital velocity scres a hit.
    def test_initial_velocity(self, change_x, change_y):
        x = 0
        y = 0
        peak_height = -1 * float("inf")
        
        # iterate through the steps
        landed = False
        # ensuring it is within bounds
        while x <= self.right_end and y >= self.bottom_end:
            peak_height = max(y, peak_height)
            if self.hit(x, y):
                landed = True
                break
            # goto next position
            x += change_x
            y += change_y
            change_x = decreaseMagnitute(change_x)
            change_y -= 1

        return (landed, peak_height)

    # did it hit?
    def hit(self, x, y):
        return x >= self.left_end and x <= self.right_end and y >= self.bottom_end and y <= self.top_end

    # find the greatest peak height
    def highest_peak_height(self):
        peak_height = -1 * float("inf")
        for x, y in self.calculatedTrajectories:
            peak_height = max(self.test_initial_velocity(x, y)[1], peak_height)

        return peak_height

f = open("Q17/Q17_input.txt")
points = ProbeTrajectorySolver(f.read())

trajectory = points.get_initial_velocity()
print("part 1:",points.highest_peak_height())  
print("part 2:",len(set(trajectory)))  