N = int(input())
li = []
for i in range(0,N):
    li.append(int(input()))
li.sort()
li = list(map(str, li))
print('\n'.join(li))