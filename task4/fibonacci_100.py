n1 = 0
n2 = 1
n = 0

fibe_list = [0, 1]

while n1 + n2 <= 100:
    n = n1 + n2

    fibe_list.append(n)
    n1 = n2
    n2 = n

print(fibe_list)
