n = int(input())
a = sorted(list(map(int, input().split())))
avg = a[n//2] if n%2==1 else round((a[n//2]+a[n//2-1])/2)
ans = (10**5, 0)
for i in [0, 1, -1]:
    bar = avg + i
    cost = sum(abs(bar - a[k]) - 1 if abs(bar - a[k]) > 1 else 0 for k in range(n))
    if cost < ans[0]:
        ans = (cost, bar)
print(f'{ans[1]} {ans[0]}')