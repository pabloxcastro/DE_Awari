fruits = ["bananas", "maçãs", "peras", "uvas", "laranjas"]

opc = "uvas"

while opc != "999":
    if opc not in fruits:
        fruits.append(opc)

    opc = input("Fruta?")


print(fruits)
