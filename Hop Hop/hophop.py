#Hop Hop by Frog

n = int(input("n: "))

for i in range(n):
    instants = int(input("No. of Instants: "))
    pos = 0
    positions = []

    for t in range(1,instants+1):
        if t % 2 != 0:
            pos = pos + 2
            positions.append(pos)
        elif t % 2 == 0:
            pos = pos - 1
            positions.append(pos)

        print(positions)

    print("Farthest Point reached: ",max(positions))
