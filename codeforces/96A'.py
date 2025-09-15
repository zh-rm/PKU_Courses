def a(z):
    return max(len(i) for i  in b.split(z)) > 6
b = input()
print("YES" if a('0') or a('1') else "NO")

# 10min，不能用a(z)然后return 'z'要用f'{z}'