a= int(input())
li=[]
for i in range(a):
    li.append(int(input()))
for i in li:
    if i>= 34:
        print('0')
    else:
        ans=1
        for j in range(1,i+1):
            ans*=j
        print(str(ans%(2**32)))