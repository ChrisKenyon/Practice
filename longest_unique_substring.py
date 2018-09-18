## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

# find longest unique substring in a string
# example = "abdecdrtyuio"  len 12
# answer = "ecdrtyuio"
#

# 'aaaaaaaaaaaa'

def longest_unique_substring(string):
    '''
         Input: string (str)
         Output: (str)
         Return the longest unique substring within the input string
    '''
    start, end = (0, 0)
    subset = set()
    longest_sub = ''

    while end < len(string):

        char = string[end]
        if char not in subset:
            subset.add(char)
            end += 1
            if len(subset) > len(longest_sub):
                longest_sub = string[start:end]
        else:
            subset = set()
            while string[start] != char:
                start+=1
            start+=1
            end = start

    return longest_sub


def get_counter_total(counter):
    return sum(counter.values())

def longest_unique_substring2(string):
    '''
         Input: string (str)
         Output: (str)
         Return the longest unique substring within the input
         string where one character is allowed to repeat
    '''
    start, end = (0, 0)
    subset = {s:0 for s in string}
    longest_sub = ''
    is_repeat = False
    repeat_char = ''
    while end < len(string):

        char = string[end]
        if subset[char] > 0 and !is_repeat:
            is_repeat = True
            repeat_char = char

            subset[char]+=1
            end += 1
            if get_counter_total(subset) > len(longest_sub):
                longest_sub = string[start:end]

        elif subset[char] == 0 or repeat_char == char:
            subset[char]+=1
            end += 1
            if get_counter_total(subset) > len(longest_sub):
                longest_sub = string[start:end]

        else:
            # We have found a second duplicate char
            while subset[repeat_char] > 1:
                subset[string[start]] -= 1
                start+=1

            end = start
            repeat_char = char
            subset[char]+=1

    return longest_sub
