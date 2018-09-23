def findstring(k, seq):
    string=''
    for i in range(len(seq)):
        if seq[i]>k:
            string+='0'
        else:
            string+='1'
            k-=seq[i]
    return string
        
tcases=int(raw_input())
for i in range(tcases):
    n, k= map(int, raw_input().split(' '))
    seq=map(int, raw_input().split(' '))
    fin=findstring(k, seq)
    print fin
