lines=open('atlanin.txt','r').readlines()
n=int(lines[0])
li=[int(i) for i in lines[1:]]
'''
lif=[li[0]]
lib=[]
for i in range(1,len(li)):
    lif.append(max(lif[i-1],li[i]))
temp = li[-1]
for i in reversed(li):
    temp=max(temp, i)
    lib.append(temp)
lib.reverse()
ans=0
for i in range(1,len(li)-1):
    if li[i]<lif[i-1] and li[i]<lib[i+1]:ans+=1
'''
ml,mr=0,0
ans=0
left=[False]*int(1e6+1)
right=[False]*int(1e6+1)
for i in range(n):
    if mr>li[i]:
        right[i]=True
    else:
        mr=li[i]
for i in range(n-1,-1,-1):
    if ml>li[i]:
        left[i]=True
    else:
        ml=li[i]
for i in range(n):
    if left[i]==True and right[i]==True:ans+=1
open("atlanout.txt","w").write(str(ans))