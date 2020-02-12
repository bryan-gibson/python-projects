
bribes = 0 

arr = []
for x in range(10):
    arr.append(x+1)

for y in range(len(arr)):
    if arr[y] > (y+3):
        return ("Too chaotic")
    else:
        bribes += ((y+3) - arr[y])
return bribes

print (arr)


for j in range(max(q[i]-MAX,0), i):
        if q[j] > q[i]: bribes += 1