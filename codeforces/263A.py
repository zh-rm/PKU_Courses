for i in range(5):
    row = list(map(int,input().split()))
    if sum(row)==1:
        i0 = i
        j0 = row.index(1)
        break
print(abs(i0-2)+abs(j0-2))