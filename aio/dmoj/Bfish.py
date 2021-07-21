C= int(input())
FC=0
for i in range(C):
    a,b=[int(j) for j in input().split()]
    if a*b>FC:
        FC=a*b
N= int(input())
FN=0
for i in range(N):
    a,b=[int(j) for j in input().split()]
    if a*b>FN:
        FN=a*b
if FC>FN:
    print('Casper')
elif FC<FN:
    print('Natalie')
else:
    print('Tie')