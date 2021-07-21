infile = open('pairin.txt','r')
N = int(infile.readline().strip())
dic = {}
t = 0
for i in range(0,2*N):
    c=infile.readline().strip()
    if c in dic:
        if i-dic[c]>t:
                t = i-dic[c]
    elif c not in dic:
        dic[c]=i

outfile = open('pairout.txt','w')
outfile.write(str(t))
outfile.close()