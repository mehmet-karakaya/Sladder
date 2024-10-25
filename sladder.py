import random

endPoint = 100
p1Place = 0
p2Place = 0
p3Place = 0
i = 1
currPlayer = "p"+ str(i)
upperSpots = [[20, 39], [30, 53], [37, 65], [59, 78], [69, 86], [85, 94]]
lowerSpots = [[96, 2], [54, 7], [25, 9], [41, 21], [70, 31], [83, 38], [79, 42], [92, 64]]

def dice():
	return random.choice([1,2,3,4,5,6])

def checkUpper(place):
	j = 0
	for x in range(len(upperSpots)):
		print(x)

def checkLower(place):
	j = 0
	for x in range(len(lowerSpots)):
		print(x)

def checkSpots(place):
	global upperSpots, lowerSpots, p1Place, p2Place, p3Place
	if (checkUpper(player, place)):
		
	else:
		checkLower(player, place)

def playerTurn(player):
	global p1Place, p2Place, p3Place
	if player == "p1":
		p1Place += dice()
		checkSpots(p1Place)
	elif player == "p2":
		p2Place += dice()
		checkSpots(p2Place)
	elif player == "p3":
		p3Place += dice()
		checkSpots(p3Place)
	nextPlayerTurn()

def nextPlayerTurn():
	global i, currPlayer
	i += 1
	if i > 3:
		i = 1
	currPlayer = "p" + str(i)

while (p1Place < endPoint and p2Place < endPoint and p3Place < endPoint):
	playerTurn(currPlayer)
	
	
