n , k = map(int , input().split())
score = sorted(list(map(int, input().split())))
while score[0] < score[-k]:
    del score[0]
if score[-1] == 0:
    print(0)
else:
    while score[0] == 0:
        del score[0]
    print(len(score))