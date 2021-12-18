def probx(a,b):
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
    if a>1 and b>0 and (a<3 or b<2):
        print(a,":",b-1,"=",win/100000,"   ",a-1,":",b,"=",else1/100000)
    elif a>2 and b>1 and (a<4 or b<3):
        print(a,":",b-2,"=",win/100000,"   ",a-1,":",b-1,"=",else1/100000,"   ",a-2,":",b,"=",else2/100000)
    elif a>3 and b>2:
        print(a,":",b-3,"=",win/100000,"   ",a-1,":",b-2,"=",else1/100000,"   ",a-2,":",b-1,"=",else2/100000,"   ",a-3,":",b,"=",else3/100000)
    else:
        print(a,":",b,"=",win/100000)
