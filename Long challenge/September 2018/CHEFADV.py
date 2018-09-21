tcases=int(raw_input())
for _ in xrange(tcases):
    n, m, x, y = map(int, raw_input().split(' '))
    if m==1 and n==1:
        print "Chefirnemo"
        continue
    n-=1
    m-=1
    if (n>=0 and n%x==0) and (m>=0 and m%y==0):
        print "Chefirnemo"
    else:
        n-=1
        m-=1
        if (n>=0 and n%x==0) and (m>=0 and m%y==0):
            print "Chefirnemo"
            continue
        print "Pofik"
