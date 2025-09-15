for _ in range(int(input())):
    w = input()
    L = ''
    k = 0
    n = len(w)
    for i in range(n):
        if w[i] != '0':
            L = L + w[i] + '0'*(n - 1 -i) + ' '
            k += 1
    print(k)
    print(L[:-1])