test1 = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
test2 = [1,1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
test3 = [1,1,1,2,2,2,3,3,4,4,4,5,5,5,6,6,6]
test4 = [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6,6,6]
test5 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,6]
test6 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6]
test7 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]

test8 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7]
test9 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,6,7,7,7]
test10 = [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6,6,6,7,7,7]
test11 = [1,1,1,2,2,2,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
test12 = [1,1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
test13 = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]

def find_missing(a):
    l = 0
    r = len(a) - 1
    while r - l > 2:
        m = l + (r-l) // 2
        if a[m] == a[m-2]:
            m -= 2
        elif a[m] == a[m-1]:
            m -= 1
        if m%3 != 0:
            r = m - 1
        elif not (a[m] == a[m+1] == a[m+2]):
            return a[m]
        else:
            l = m + 3
    return a[l]

print(find_missing(test1))
print(find_missing(test2))
print(find_missing(test3))
print(find_missing(test4))
print(find_missing(test5))
print(find_missing(test6))
print(find_missing(test7))
print(find_missing(test8))
print(find_missing(test9))
print(find_missing(test10))
print(find_missing(test11))
print(find_missing(test12))
print(find_missing(test13))
