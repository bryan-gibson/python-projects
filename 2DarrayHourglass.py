"""
This program finds the "hourglasses" within a 2d array and calculates the highest 
among them.

Hourglass Ex.
2 1 3
  4
5 3 2
"""

import random

# Creates an array containing 6 lists, each of 6 items
w, h = 6, 6

arr = [[random.randrange(-9, 9) for x in range(w)] for y in range(h)]

#array to store Hourglass Sums
hgSum = []

#print (arr)

#outputs array in format
for x in range(len(arr[0])):
    print (arr[x])

#iterates through 2d array and calculates hourglass sums
for x in range(len(arr)):
    for y in range(len(arr[0])):
        if x > 0 and x < 5:
            if y > 0 and y < 5:
                #adds sums to sum array
                hgSum.append(arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1]
                    + arr[x][y] + arr[x+1][y-1] + 
                    arr[x+1][y] + arr[x+1][y+1])

#print (hgSum)

highNum = hgSum[0]

#finds highest sum in hgSum array
for z in range(len(hgSum)):
    if hgSum[z] > highNum:
        highNum = hgSum[z]

print (highNum)
