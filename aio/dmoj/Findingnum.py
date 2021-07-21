'''timeout
n,M=[int(i) for i in input().split()]
A=input().split()
A= list(map(int,A))
tot=0
for i in range(n-1):
    for j in range(i+1,n):
        if A[i]+A[j] <= M:
            tot+=1
print(str(tot))
'''
def func(num,mi,ma,tl,th):
    temp=(mi+ma)//2
    if A[num]+A[temp]<=M:
        if temp+1==n:
            print('a'+ str(n-num-1))
            return n-num-1
        if temp+1 in th:
            if temp<=num:
                return 0
            else:
                return temp-num+1
        else:
            tl.append(temp)
            return func(num,temp,ma,tl,th)
    else:
        if temp-1<0:
            print(0)
            return 0
        if temp-1 in tl:
            print('d'+str(temp-num))
            return temp-num
        else:
            print(tl)
            th.append(temp)
            return func(num,mi,temp,tl,th)
n,M=[int(i) for i in input().split()]
A=list(input().split())
A= list(map(int,A))
tl=[]
th=[]
A.sort()
tot=0
for i in range(n):
    tot+=func(i,0,n,tl,th)
    tl=[]
    th=[]
print(str(tot))