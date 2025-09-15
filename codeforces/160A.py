n = int(input())
l = sorted(list(map(int, input().split())))[::-1]
l += [0]
s = sum(l)
for i in range(n+1):
    if sum(l[:i])*2 > s:
        print(i)
        break