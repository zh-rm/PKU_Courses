def a(z):
    return len(sorted(b.split(z))[-1]) > 6
b = input()
print("YES" if a('0') or a('1') else "NO")