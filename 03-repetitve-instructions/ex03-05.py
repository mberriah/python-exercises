i = 1

while(i <= 20):
    print(7 * i, end="")
    if((7 * i) % 3 == 0):
        print("*", end="")
    print(end=" ")
    i = i + 1
