for _ in range(int(input())):
    n = int(input())
    a, b = sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())))
    print(min(b[0] * n + sum(a), a[0] * n + sum(b)))

#5 min