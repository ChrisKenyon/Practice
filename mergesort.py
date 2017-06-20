def merge(l,m,r):
    arr1 = array[l:m][::-1]
    arr2 = array[m:r][::-1]
    while l < r:
        if len(arr1) > 0 and len(arr2) > 0:
            array[l] = arr1.pop() if arr1[-1] < arr2[-1] else arr2.pop()
            #array[l] = arr1.pop(0) if arr1[0] < arr2[0] else arr2.pop(0)
        else:
            array[l] = arr1.pop() if len(arr1) > 0 else arr2.pop()
            #array[l] = arr1.pop(0) if len(arr1) > 0 else arr2.pop(0)
        l+=1
def mergesort(l,r):
    if r - l <= 1:
        return
    m = (l + r)/2
    mergesort(l,m)
    mergesort(m,r)
    merge(l,m,r)

if __name__==='__main__':
    array = [5,2,1,8,3,6,9,10,100,50,30,20,40]
    import sys
    if sys.argv[1:]:
        array = map(int,sys.argv[1:])
    mergesort(0, len(array))
    print array
