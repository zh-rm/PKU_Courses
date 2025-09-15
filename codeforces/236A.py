name = input()
list = set()
list.update(i for i in name)
if len(list) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")