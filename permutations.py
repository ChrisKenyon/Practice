def all_perm(string):
    perms = [[]]*len(string)
    perms[0] = [string[0]]
    for c in range(1,len(string)):
        letter=string[c]
        new_perms = []
        for perm in perms[c-1]:
            for i in range(len(perm)+1):
                tmp = perm[:i]+letter+perm[i:]
                new_perms.append(tmp)
        perms[c]=new_perms
    print len(perms[c]), perms[c]

def all_perm_no_dup(string):
    perms = [[]]*len(string)
    perms[0] = [string[0]]
    for c in range(1,len(string)):
        letter = string[c]
        hash_set = set()
        for perm in perms[c-1]:
            for i in range(len(perm)+1):
                tmp = perm[:i]+letter+perm[i:]
                if tmp not in hash_set:
                    hash_set.add(tmp)
        perms[c] = list(hash_set)
    print len(perms[c]), perms[c]

import sys
test_string = sys.argv[1]
print 'All permutations: '
all_perm(test_string)
print 'All permutations without duplicates'
all_perm_no_dup(test_string)
