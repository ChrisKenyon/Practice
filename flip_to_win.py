def flip_to_win(val):
    flipped = False
    max_ones = 0
    current_string = 0
    for i in range(32):
        if val&1:
            current_string += 1
        elif flipped:
            current_string = 0
        else:
            current_string+=1
            flipped = True
        max_ones = max(current_string, max_ones)
        val>>=1
    return max_ones
import sys
val = int(sys.argv[1])
print flip_to_win(val)
