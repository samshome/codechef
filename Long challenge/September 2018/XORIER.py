def check(num):
    count=0
    j=0
    while(j+1<len(num)):
        ntimes=1
        if num[j]==num[j+1]:
            while(j+1<len(num)):
                if num[j]==num[j+1]:
                    ntimes+=1
                    j+=1
                else:
                    break
        if j+1>len(num)-1:
            break
        if num[j]%4==0 or num[j]%4==1:
            if num[j]==num[j+1]-2:
                temp=j+1
                ntimes2=1
                if j+2<len(num):
                    while(j+2<len(num)):
                        if num[j+1]==num[j+2]:
                            j+=1
                            ntimes2+=1
                        else:
                            j+=1
                            break
                else:
                    j+=1
            else:
                temp=j+1
            if j==len(num)-2 and ntimes>1:
                count+=ntimes*(len(num)-(j+2))
            else:
                count+=ntimes*(len(num)-(j+1))
            j=temp
        else:
            count+=ntimes*(len(num)-(j+1))
            j+=1
    return count

        
    
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def sort(arr,l,r):
    if l < r:
        m = (l+(r-1))/2
        sort(arr, l, m)
        sort(arr, m+1, r)
        merge(arr, l, m, r)
    
def findsum(odd, even):
    total=0
    sort(odd, 0, len(odd)-1)
    sort(even,0, len(even)-1)
    total+=check(odd)
    total+=check(even)
    print total
    
tcases=int(raw_input())
for _ in xrange(tcases):
    n=int(raw_input())
    odd=[]
    even=[]
    num=map(int, raw_input().split())
    for i in xrange(len(num)):
        if num[i]%2==0:
            even.append(num[i])
        else:
            odd.append(num[i])
    if len(num)==n:
        findsum(odd, even)
