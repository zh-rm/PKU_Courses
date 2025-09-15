i = 0
for _ in range(int(input())):
    if sum(map(int, input().split())) > 1:
        i += 1 
print(i)