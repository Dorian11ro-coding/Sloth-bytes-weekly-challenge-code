def makeBox(n):
    box = []

    if n == 1:
        box.append("#")
    else:
        box.append("#" * n)

        for i in range(n - 2):
            box.append("#" + " " * (n-2) + "#")

        box.append("#" * n)

    return box

size = int(input("How big: "))
box = makeBox(size)
for row in box:
    print(row)
