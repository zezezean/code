infile=open('rpsin.txt','r')
outfile=open('rpsout.txt','w')
pnt=0
def win(p,l,w):
    temp=min(l,w)
    p+=temp
    l-=temp
    w-=temp
    return p,l,w
    
def lose(p,l,w):
    temp=min(l,w)
    p-=temp
    return p,l,w
n=infile.readline().strip()
ra,pa,sa=map(int,infile.readline().split())
rb,pb,sb=map(int,infile.readline().split())
pnt,ra,pb=win(pnt,ra,pb)
pnt,pa,sb=win(pnt,pa,sb)
pnt,sa,rb=win(pnt,sa,rb)
pnt,pa,rb=lose(pnt,pa,rb)
pnt,sa,pb=lose(pnt,sa,pb)
pnt,ra,sb=lose(pnt,ra,sb)

outfile.write(str(pnt))
outfile.close()
