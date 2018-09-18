heights = [2,0,1,0,3,2,1,0,2,3]
#heights = [0,1,0,2,1,0,1,3,2,1,2,1]
#heights = [3,0,0,2,0,0,1,0]
'''
start = 0
start_idx = 0
potential = 0
total_fill = 0
occupied = 0
highest_close = 0
highest_close_idx = 0
i = 0
import pdb
while i < len(heights):
    curr = heights[i]
    pdb.set_trace()
    if curr > start:
        total_fill += potential
        potential = 0
        start = curr
        start_idx = i
        occupied = 0
    elif curr == start:
        total_fill += potential
        potential = 0
        occupied = 0
    elif curr < start:
        # THIS IS ALL WRONG
        pot_rem = (start - curr) * (i - start_idx - 1)
        pot_mid_fill = potential - pot_rem - occupied
        if pot_mid_fill > 0:
            total_fill += pot_mid_fill
            potential -= pot_mid_fill
            occupied+= pot_mid_fill
        potential += start-curr
        occupied += curr
    i+=1
print total_fill
'''
import pdb
left = [0]*len(heights)
right = [0]*len(heights)
left[0] = heights[0]
right[-1] = heights[-1]
fill = 0
# make a left array showing the highest to the left
for i in range(1,len(heights)):
    left[i] = max(left[i-1], heights[i])
# make a right array showing the highest to the right
for i in range(len(heights)-2,-1,-1):
    right[i] = max(right[i+1],heights[i])
# find the max you can fill in each spot, the min highest
# to both the left and right
for i in range(len(heights)):
    fill += min(left[i],right[i]) - heights[i]

print fill
