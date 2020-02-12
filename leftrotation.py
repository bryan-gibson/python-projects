"""
A left rotation operation on an array shifts each of the array's elements 1
unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5],
then the array would become [3,4,5,1,2].

Given an array a of n integers and a number, d, perform d left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.
"""

import random

arr = [random.randrange(10) for x in range(5, 10)]
num_Rot = random.randrange(1, 10)


print (arr)
print ("Rotating left " + str(num_Rot) + " times")

temp = 0

for x in range(num_Rot):
    temp = arr[-1]
    for y in range(len(arr) - 1):
        if y == 0:
            arr[-1] = arr[y]
        arr[y] = arr[y+1]
    arr[-2] = temp

#arr[num_Rot:] + arr[:num_rot] // Optimized version
        
print (arr)
    

