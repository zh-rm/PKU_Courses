a = input().lower()
b = input().lower()
n = len(a)
if a == b:
    print(0)
else:
    for i in range(n):
        if ord(a[i]) > ord(b[i]):
            print(1) 
            break
        elif ord(a[i]) < ord(b[i]):
            print(-1)
            break
