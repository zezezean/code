n = int(input())
k = int(input())
piemap = dict()
def pie(pieces, people):
    if pieces < people:
        print('0')
        return 0
    if people == 1 or pieces == people:
        print('1')
        return 1
    if (pieces, people) in piemap:
        print(piemap[(pieces, people)])
        return piemap[(pieces, people)]
    piemap[(pieces, people)] = pie(pieces - 1, people - 1) + pie(pieces - people, people)
    print(piemap[(pieces, people)])
    return piemap[(pieces, people)]


print(pie(n, k))