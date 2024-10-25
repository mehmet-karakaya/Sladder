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
	global upperSpots
	for x in range(len(upperSpots)):
		if place == upperSpots[x][0]:
			return upperSpots[x][1]
	return -1

def checkLower(place):
	global lowerSpots
	for x in range(len(lowerSpots)):
		if place == lowerSpots[x][0]:
			return lowerSpots[x][1]
	return -1

def checkSpots(player, place):
	global p1Place, p2Place, p3Place
	x = checkUpper(place)
	if x < 0:
		x = checkLower(place)
	if x > 0:
		if player == "p1":
			p1Place = x
		elif player == "p2":
			p2Place = x
		elif player == "p3":
			p3Place = x

def playerTurn(player):
	global p1Place, p2Place, p3Place
	if player == "p1":
		p1Place += dice()
		if p1Place >= 100:
			p1Place = 100
			print("Player 1 is the winner")
			return
		checkSpots(player, p1Place)
	elif player == "p2":
		p2Place += dice()
		if p2Place >= 100:
			p2Place = 100
			print("Player 2 is the winner")
			return		
		checkSpots(player, p2Place)
	elif player == "p3":
		p3Place += dice()
		if p3Place >= 100:
			p3Place = 100
			print("Player 3 is the winner")
			return
		checkSpots(player, p3Place)
	nextPlayerTurn()

def nextPlayerTurn():
	global i, currPlayer
	i += 1
	if i > 3:
		i = 1
	currPlayer = "p" + str(i)


while (p1Place < endPoint and p2Place < endPoint and p3Place < endPoint):
	playerTurn(currPlayer)


