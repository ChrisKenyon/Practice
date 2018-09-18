# array of length n of non-repeating, non-sorted, unique ints
# with the addition of one number, the array becomes a consequtive
# sequence when sorted that starts at 1
# find that number

def find_missing(arr):
    return sum(arr)-sum(range(1,len(arr)))


