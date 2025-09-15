def AB(i):
    R = int(i[br:])
    C = sum([(ord(i[kk])-ord("A") + 1) * 26 ** (br - kk - 1) for kk in range(br)])
    return f"R{R}C{C}"
def BA(i):
    list = ""
    R = i[1:k]
    C = int(i[k+1:])
    while C != 0 :
        if C % 26 == 0:
            list = "Z" + list
            C = C//26 - 1
        else:
            list = chr(C % 26 + ord('A') - 1) + list
            C = C//26

    return list + R

n = int(input())
for _ in range(n):
    cell_input = input()
    k = 0
    state = 1
    while k+1 < len(cell_input) and state:
        if cell_input[k].isdigit() and cell_input[k+1].isalpha():
            state = 0 
        if cell_input[k+1].isdigit() and cell_input[k].isalpha():
            br = k + 1
        k += 1
    if state:
        print(AB(cell_input))
    else:
        print(BA(cell_input))

