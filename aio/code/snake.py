des=list(map(int,open('snakein.txt','r').readline().split()))
cur=[0]*2
ans=''
drct='u'
while cur!=des:
    if not len(ans)%2:
        if des[0]<cur[0]:
            if drct=='u':
                ans+='L'
            else:
                ans+='R'
            drct='l'
            cur[0]-=1
        else:
            if drct=='u':
                ans+='R'
            else:
                ans+='L'
            drct='r'
            cur[0]+=1
    else:
        if des[1]<cur[1]:
            if drct=='l':
                ans+='L'
            else:
                ans+='R'
            drct='d'
            cur[1]-=1
        else:
            if drct=='l':
                ans+='R'
            else:
                ans+='L'
            drct='u'
            cur[1]+=1
open('snakeout.txt','w').write(str(ans))