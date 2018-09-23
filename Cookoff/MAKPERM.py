def findnext(num, sequence):
    newseq=[0 for i in range(num+1)]
    count=0
    for i in range(num):
        if sequence[i]>num:
            continue
        else:
            newseq[sequence[i]]+=1
    for k in range(1, num+1):
        if newseq[k]==0:
            count+=1
    return count
tcases=int(raw_input())
for i in range(tcases):
    num=int(raw_input())
    sequence=map(int, raw_input().split())
    fin=findnext(num, sequence)
    print fin
