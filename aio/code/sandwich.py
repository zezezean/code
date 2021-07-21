infile = open("holesin.txt",'r').readlines()
l,w=map(int,infile[0].split())
a,b=map(int,infile[1].split())
open("holesout.txt",'w').write(str((l//a)*(w//b))).close()