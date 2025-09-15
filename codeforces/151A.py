n,k,l,c,d,p,L,P=map(int, input().split())
print(int(min(k*l/L, c*d, p/P)) // n)