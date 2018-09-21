inparray=range(1,int(raw_input())+1)
leng=len(inparray)
midl=leng/2
ans=[]
lans=[inparray[leng-1]]
if leng!=1:
    
    for i in xrange(1, midl):
        ans.append(inparray[i])
    ans.append(1)
    for k in xrange(midl+1, leng):
        ans.append(inparray[k])
    ans.append(inparray[leng/2])
    print " ".join(str(j) for j in ans)

    for i in xrange(0, leng-1):
        lans.append(inparray[i])

    print " ".join(str(j) for j in lans)

else:
    print '1'
    print '1'




