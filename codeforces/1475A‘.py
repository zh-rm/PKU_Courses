import math
for _ in range(int(input())):
    print('NO' if math.log2(int(input())).is_integer() else 'YES')