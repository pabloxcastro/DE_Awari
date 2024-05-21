n = 1024
list_fatores = []
div = 2

while n > 1:
    if n % div == 0:
        list_fatores.append(div)
        n = n / div
    else:
        div += 1

print(list_fatores)
