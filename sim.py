def sim(a,b): # simulate a battle between two bordering regions with army sizes a and b
	import random
	if a>1:
		global die1#roll
		die1=random.randint(1,6)
	if a>2:
		global die2
		die2=random.randint(1,6)
	if a>3:
		global die3
		die3=random.randint(1,6)
	if b>0:
		global die4
		die4=random.randint(1,6)
	if b>1:
		global die5
		die5=random.randint(1,6)
	if b>2:
		global die6
		die6=random.randint(1,6)
	global list1#list create
	if a==2:
		list1=[die1]
	if a==3:
		list1=[die1,die2]
	if a>3:
		list1=[die1,die2,die3]
	global list2
	if b==1:
		list2=[die4]
	if b==2:
		list2=[die4,die5]
	if b>2:
		list2=[die4,die5,die6]
	if a>2:#list sort
		list1.sort(reverse=True)
	if b>1:
		list2.sort(reverse=True)
	global p#def points
	global q
	p=0
	q=0
	if a>1 and b>0:
		if list1[0]>list2[0]:#compare rolls
			p=p+1
		else:
			q=q+1
	if a>2 and b>1:
		if list1[1]>list2[1]:
			p=p+1
		else:
			q=q+1
	if a>3 and b>2:
		if list1[2]>list2[2]:
			p=p+1
		else:
			q=q+1
	global troopsleft1#subtract points from opponent
	global troopsleft2
	troopsleft1=a-q
	troopsleft2=b-p
