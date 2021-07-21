n=int(input())
qk='aeiou'
pre,l,pres='',0,[]
for i in range(n):
    s=input().split()
    kk=['']*len(s)
    for j in range(len(s)):
        if len(s[j])>2 and s[j][0] not in qk:
            for k in s[j]:
                if k not in qk:
                    pre+=k
                    l+=1
                else:
                    pres.append(pre)
                    pre=''
                    kk[j]=s[j][l:]
                    l=0
                    break
    x,ans=-1,''
    for j in range(len(s)):
        if len(s[j])>2 and s[j][0] not in qk:
            ans+=pres[x]+kk[j]
            x+=1
        else:
            ans+=s[j]
        ans+=' '
    print(ans)
    kk,pres=[],[]