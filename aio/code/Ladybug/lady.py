#lines=open("ladyin.txt","r").readlines()
#li=[int(i) for i in lines[1:]]
lines=open("ladyin.txt","r")
li=[]
for i in lines:
    li.append(int(i.strip()))
del li[0]
ans=max(li)-min(li)+1
out=open("ladyout.txt","w")
out.write(str(ans))
out.close()