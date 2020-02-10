import random

# Creates a list containing 6 lists, each of 6 items
w, h = 6, 6

Matrix = [[random.randrange(5) for x in range(w)] for y in range(h)]
hgSum = []

print (Matrix)

for x in range(6):
    for y in range(6):
        if x > 0 and x < 5:
            if y > 0 and y < 5:
                hgSum.append(Matrix[x-1][y-1] + Matrix[x][y-1] + Matrix[x+1][y-1] + Matrix[x][y] + Matrix[x-1][y+1] +
                    Matrix[x][y+1] + Matrix[x+1][y+1])

print (hgSum)

highNum = 0

for z in range(len(hgSum)):
    if hgSum[z] > highNum:
        highNum = hgSum[z]

print (highNum)
