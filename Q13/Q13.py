import matplotlib.pyplot as plt

f = open("Q13/Q13_input.txt", "r")
points = []
folds = []

# getting the points and the folding instructions into seperate arrays
x = f.readline().strip()
while (x != ""):
    x = [int(coord) for coord in x.split(",")]
    points.append(tuple(x))
    x = f.readline().strip()

points = list(set(points))

for x in f.readlines():
    x = x.strip().split(" ")[2].split("=")
    folds.append(x)

if folds[0][0] == "y":
    for point in points:
        if point[1] <= int(folds[0][1]):
            continue
        else:
            points[points.index(point)] = (point[0] , int(folds[0][1]) - (point[1] - int(folds[0][1]))) 
elif folds[0][0] == "x":
    for point in points:
        if point[0] <= int(folds[0][1]):
            continue
        else:
            points[points.index(point)] = (int(folds[0][1]) - (point[0] - int(folds[0][1])), point[1]) 

points = list(set(points))
print(len(points))

for fold in folds[1:]:
    if fold[0] == "y":
        for point in points:
            if point[1] <= int(fold[1]):
                continue
            else:
                points[points.index(point)] = (point[0] , int(fold[1]) - (point[1] - int(fold[1]))) 
    elif fold[0] == "x":
        for point in points:
            if point[0] <= int(fold[1]):
                continue
            else:
                points[points.index(point)] = (int(fold[1]) - (point[0] - int(fold[1])), point[1]) 

points = list(set(points))

plt.scatter(*zip(*points))
plt.show()