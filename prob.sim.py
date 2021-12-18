def prob(a,b):
    global win
    global else1
    global else2
    global else3
    win=0
    else1=0
    else2=0
    else3=0
    for r in range(100000):
        sim(a,b)
        if a>1 and b>0 and (a<3 or b<2):
            if troopsleft1==a:
                win=win+1
            elif troopsleft1==(a-1):
                else1=else1+1
        elif a>2 and b>1 and (a<4 or b<3):
            if troopsleft1==a:
                win=win+1
            elif troopsleft1==(a-1):
                else1=else1+1
            elif troopsleft1==(a-2):
                else2=else2+1
        elif a>3 and b>2:
            if troopsleft1==a:
                win=win+1
            elif troopsleft1==(a-1):
                else1=else1+1
            elif troopsleft1==(a-2):
                else2=else2+1
            elif troopsleft1==(a-3):
                else3=else3+1
        else:
            if troopsleft1==a:
                win=win+1
    win=win/100000
    else1=else1/100000
    else2=else2/100000
    else3=else3/100000
