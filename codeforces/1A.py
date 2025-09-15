def m(p,q):
    if p%q == 0:
        return p//q
    else:
        return 1+p//q
l = list(map(int,input().split()))
print(m(l[0],l[2])*m(l[1],l[2]))