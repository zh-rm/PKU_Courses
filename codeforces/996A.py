m = int(input())
k, m = m//100, m % 100
k, m = k + m//20, m % 20
k, m = k + m//10, m % 10
k, m = k + m//5, m % 5
print(k + m)