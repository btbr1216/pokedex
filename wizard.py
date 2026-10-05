
def wizard(owner, switchtimes, duels):
    for i in range(switchtimes):
        if duels[i][1] == owner:
            owner = duels[i][0]
    print(owner)


wizard("A", 3, ["BA", "CB", "DA"])