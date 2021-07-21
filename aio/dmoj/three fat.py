N = int(input())
li = []
for i in range(0,N):
    inp = input()
    li.append(inp)
for i in li:
    ans = 192
    while True:
        if (ans**3)%1000==888 and ans >int(i):
            print(str(ans))
            break
        ans+=10