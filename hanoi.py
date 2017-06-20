N = 100
tower1 = range(1,N+1)[::-1]
tower2 = []
tower3 = []

def move(n, orig, dest, buff):
    if n <= 0:
        return
    move(n-1,orig,buff,dest)
    dest.append(orig.pop())
    #print("T1: {} | T2: {} | T3: {}".format(str(tower1),str(tower2),str(tower3)))
    move(n-1,buff,dest,orig)

if __name__=="__main__":
    move(N,tower1,tower2,tower3)
    print("T1: {} | T2: {} | T3: {}".format(str(tower1),str(tower2),str(tower3)))
