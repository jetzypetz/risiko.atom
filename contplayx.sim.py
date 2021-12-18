def contplayx(a,b):
    print(a,b)
    sim(a,b)
    print(troopsleft1,troopsleft2)
    while troopsleft1>1 and troopsleft2>0:
        sim(troopsleft1,troopsleft2)
        print(troopsleft1,troopsleft2)
