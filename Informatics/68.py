
n = input()
a = list(map(int, input().split()))
s = 0
for i in range(1, len(a) - 1):
    s += a[i - 1] < a[i] > a[i + 1]

print(s)
