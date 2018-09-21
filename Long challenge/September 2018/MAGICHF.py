tcases=int(raw_input())
for _ in xrange(tcases):
    n, x, s= map(int, raw_input().split(' '))
    gold=x
    for _ in xrange(s):
        swap=map(int, raw_input().split(' '))
        if swap[0]==gold:
            gold=swap[1]
            continue
        elif swap[1]==gold:
            gold=swap[0]
    print gold
