
s = 0
a = map(int, input().split())
p = a.__next__()
for i in a:
    if i > p:
        print(i)
    p = i