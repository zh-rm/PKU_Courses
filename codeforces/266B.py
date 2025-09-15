n, i = map(int, input().split())
s = list(input())
for _ in range(i):
    k = 0
    while k < n - 1:
        if s[k] == "B" and s[k+1] == "G":
                s[k], s[k+1] = s[k+1], s[k]
                k += 1
        k += 1
print("".join(s))