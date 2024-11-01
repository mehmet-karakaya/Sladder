import random
''' Pygame Option
import pygame, sys
'''
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


endPoint = 100
p1Place = 0
p2Place = 0
p3Place = 0
p4Place = 0
p5Place = 0
pUptPlace = 0
p1Name = "p1"
p2Name = "p2"
p3Name = "p3"
p4Name = "p4"
p5Name = "p5"
diceRolled = 0
i = 0
playerCount = 0
maxPlayer = 5
playerNames = [p1Name, p2Name, p3Name, p4Name, p5Name]
currPlayer = playerNames[i]
inputtxt = ""
inputFromUser = ""
frame = ""
jumpPoint = 0
upperSpots = [[20, 39], [30, 53], [37, 65], [59, 78], [69, 86], [85, 94]]
lowerSpots = [[96, 2], [54, 7], [25, 9], [41, 21], [70, 31], [83, 38], [79, 42], [92, 64]]
# to move +1 to x: +61, to move +1 to y: -51
certainSpots = [[61, -102], [-122,-153], [61, -153], [61, -102], [-61, -102], [-183, -102], \
				[-244, 510], [0, 255], [246, 102], [0, 102], [0, 153], [-122, 253], [0, 153], [61, 153]]
startPoints = [	[35, 735, 50, 750], \
				[55, 735, 70, 750], \
				[35, 752, 50, 767], \
				[55, 752, 70, 767], \
				[72, 742, 87, 757]]

waitingPoints = [[70, 50, 85, 65], \
				[45, 70, 60, 85], \
				[55, 95, 70, 110], \
				[85, 95, 100, 110], \
				[95, 70, 110, 85]]

inGamePoints = [[3, 700, 18, 715], \
				[3, 720, 18, 735], \
				[3, 740, 18, 755], \
				[3, 760, 18, 775], \
				[3, 780, 18, 795]]

colors = [	["#9c5708", "#f05133"], \
			["#9c5708", "#ffd200"], \
			["#9c5708", "#2d91f0"], \
			["#9c5708", "#136f13"], \
			["#9c5708", "#eda727"]]
redPlayer = ""
yellowPlayer = ""
bluePlayer = ""
greenPlayer = ""
orangePlayer = ""
playerCircles = [redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer]


def dice():
	global diceRolled, rolledDice
	diceRolled = random.choice([1,2,3,4,5,6])
	rolledDice.config(text="Rolled Dice: " + str(diceRolled))
	return diceRolled

def checkUpper(place):
	global upperSpots, jumpPoint
	for x in range(len(upperSpots)):
		if place == upperSpots[x][0]:
			jumpPoint = x
			return upperSpots[x][1]
	return -1

def checkLower(place):
	global lowerSpots, upperSpots, jumpPoint
	for x in range(len(lowerSpots)):
		if place == lowerSpots[x][0]:
			jumpPoint = len(upperSpots) + x
			return lowerSpots[x][1]
	return -1

def checkSpots(player, place):
	global playerCount, playerNames, p1Name, p2Name, p3Name, p4Name, p5Name, maxPlayer, currPlayer, startPoints, canvasImage, \
		colors, playerCircles, redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, p1Place, p2Place, p3Place, p4Place, p5Place, pUptPlace, certainSpots, jumpPoint
	x = checkUpper(place)
	if x < 0:
		x = checkLower(place)
	if x > 0:
		if player == p1Name:
			canvasImage.move(redPlayer, certainSpots[jumpPoint][0], certainSpots[jumpPoint][1])
			p1Place = x
		elif player == p2Name:
			canvasImage.move(yellowPlayer, certainSpots[jumpPoint][0], certainSpots[jumpPoint][1])
			p2Place = x
		elif player == p3Name:
			canvasImage.move(bluePlayer, certainSpots[jumpPoint][0], certainSpots[jumpPoint][1])
			p3Place = x
		elif player == p4Name:
			canvasImage.move(greenPlayer, certainSpots[jumpPoint][0], certainSpots[jumpPoint][1])
			p4Place = x
		elif player == p5Name:
			canvasImage.move(orangePlayer, certainSpots[jumpPoint][0], certainSpots[jumpPoint][1])
			p5Place = x

def setPlayers(playerName):
	global playerCount, playerNames, p1Name, p2Name, p3Name, p4Name, p5Name, maxPlayer, currPlayer, startPoints, \
		colors, playerCircles, redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, waitingPoints
	if playerCount > maxPlayer:
		playerCount -= 1
		return
	if playerCount == 1:
		p1Name = playerName
		playerNames[0] = p1Name
		canvasImage.delete(redPlayer)
		redPlayer = canvasImage.create_oval(inGamePoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
		playerCircles[0] = redPlayer
	elif playerCount == 2:
		p2Name = playerName
		playerNames[1] = p2Name
		canvasImage.delete(yellowPlayer)
		yellowPlayer = canvasImage.create_oval(inGamePoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
		playerCircles[1] = yellowPlayer
	elif playerCount == 3:
		p3Name = playerName
		playerNames[2] = p3Name
		canvasImage.delete(bluePlayer)
		bluePlayer = canvasImage.create_oval(inGamePoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
		playerCircles[2] = bluePlayer
	elif playerCount == 4:
		p4Name = playerName
		playerNames[3] = p4Name
		canvasImage.delete(greenPlayer)
		greenPlayer = canvasImage.create_oval(inGamePoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
		playerCircles[3] = greenPlayer
	elif playerCount == 5:
		p5Name = playerName
		playerNames[4] = p5Name
		canvasImage.delete(orangePlayer)
		orangePlayer = canvasImage.create_oval(inGamePoints[4], outline=colors[4][0], fill=colors[4][1], width=2)
		playerCircles[4] = orangePlayer
	currPlayer = playerNames[0]

def playerTurn(player):
	global p1Place, p2Place, p3Place, p4Place, p5Place, p1Name, p2Name, p3Name, p4Name, p5Name, rolledDice, pUptPlace
	if player == p1Name:
		moveDist = dice()
		pUptPlace = p1Place
		p1Place += moveDist
		movePlayer(player, moveDist)
		rolledDiceText = rolledDice.cget("text")
		rolledDiceText = p1Name + " " + rolledDiceText
		rolledDice.config(text=rolledDiceText)
		if p1Place >= 100:
			p1Place = 100
			print(p1Name + " is the winner")
			return
		checkSpots(player, p1Place)
	elif player == p2Name:
		moveDist = dice()
		pUptPlace = p2Place
		p2Place += moveDist
		movePlayer(player, moveDist)
		rolledDiceText = rolledDice.cget("text")
		rolledDiceText = p2Name + " " + rolledDiceText
		rolledDice.config(text=rolledDiceText)
		if p2Place >= 100:
			p2Place = 100
			print(p2Name + " is the winner")
			return
		checkSpots(player, p2Place)
	elif player == p3Name:
		moveDist = dice()
		pUptPlace = p3Place
		p3Place += moveDist
		movePlayer(player, moveDist)
		rolledDiceText = rolledDice.cget("text")
		rolledDiceText = p3Name + " " + rolledDiceText
		rolledDice.config(text=rolledDiceText)
		if p3Place >= 100:
			p3Place = 100
			print(p3Name + " is the winner")
			return
		checkSpots(player, p3Place)
	elif player == p4Name:
		moveDist = dice()
		pUptPlace = p4Place
		p4Place += moveDist
		movePlayer(player, moveDist)
		rolledDiceText = rolledDice.cget("text")
		rolledDiceText = p4Name + " " + rolledDiceText
		rolledDice.config(text=rolledDiceText)
		if p4Place >= 100:
			p4Place = 100
			print(p4Name + " is the winner")
			return
		checkSpots(player, p4Place)
	elif player == p5Name:
		moveDist = dice()
		pUptPlace = p5Place
		p5Place += moveDist
		movePlayer(player, moveDist)
		rolledDiceText = rolledDice.cget("text")
		rolledDiceText = p5Name + " " + rolledDiceText
		rolledDice.config(text=rolledDiceText)
		if p5Place >= 100:
			p5Place = 100
			print(p5Name + " is the winner")
			return
		checkSpots(player, p5Place)
	nextPlayerTurn()

def nextPlayerTurn():
	global i, currPlayer, playerCount, playerNames
	i += 1
	if i > playerCount - 1:
		i = 0
	currPlayer = playerNames[i]

def rollDiceBtnFunc():
	global currPlayer, p1Place, p2Place, p3Place, p4Place, p5Place, p1Name, p2Name, p3Name, p4Name, p5Name, playerCount
	if playerCount > 0:	
		playerTurn(currPlayer)
		print(p1Name + ": " + str(p1Place) + ", " + p2Name + ": " + str(p2Place) + ", " + p3Name + ": " + str(p3Place) + ", " + p4Name + ": " + str(p4Place) + ", " + p5Name + ": " + str(p5Place))

def getInput():
	global inputtxt, frame, inputFromUser
	inp = inputtxt.get(1.0, "end-1c")
	inputFromUser = inp
	setPlayers(inputFromUser)
	frame.destroy()
	return

def addPlayerBtnFunc():
	global playerCount, maxPlayer, inputtxt, frame
	if playerCount >= maxPlayer:
		return
	playerCount += 1

	# Take new player's name from user
	frame = tk.Tk() 
	frame.title("TextBox Input") 
	frame.geometry('200x200')
	# TextBox Creation 
	inputtxt = tk.Text(frame, 
					height = 5, 
					width = 20) 
	inputtxt.pack() 
	
	# Button Creation 
	printButton = tk.Button(frame, 
							text = "Print",
							height = 3,
							width = 20,
							padx = 5,
							pady = 5,
							command = getInput)
	printButton.pack()
	resBtnFunc()

def removePlayerBtnFunc():
	global p1Place, p2Place, p3Place, p4Place, p5Place, playerCount, currPlayer, playerNames, playerCircles, redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, canvasImage, waitingPoints, colors, startPoints
	if playerCount > 0:
		playerCount -= 1
		if playerCount == 0:
			canvasImage.delete(redPlayer)
			redPlayer = canvasImage.create_oval(waitingPoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
			playerCircles[0] = redPlayer
		elif playerCount == 1:
			canvasImage.delete(redPlayer)
			canvasImage.delete(yellowPlayer)
			redPlayer = canvasImage.create_oval(inGamePoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
			yellowPlayer = canvasImage.create_oval(waitingPoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
			playerCircles[0] = redPlayer
			playerCircles[1] = yellowPlayer
		elif playerCount == 2:
			canvasImage.delete(redPlayer)
			canvasImage.delete(yellowPlayer)
			canvasImage.delete(bluePlayer)
			redPlayer = canvasImage.create_oval(inGamePoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
			yellowPlayer = canvasImage.create_oval(inGamePoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
			bluePlayer = canvasImage.create_oval(waitingPoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
			playerCircles[0] = redPlayer
			playerCircles[1] = yellowPlayer
			playerNames[2] = bluePlayer
		elif playerCount == 3:
			canvasImage.delete(redPlayer)
			canvasImage.delete(yellowPlayer)
			canvasImage.delete(bluePlayer)
			canvasImage.delete(greenPlayer)
			redPlayer = canvasImage.create_oval(inGamePoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
			yellowPlayer = canvasImage.create_oval(inGamePoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
			bluePlayer = canvasImage.create_oval(inGamePoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
			greenPlayer = canvasImage.create_oval(waitingPoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
			playerCircles[0] = redPlayer
			playerCircles[1] = yellowPlayer
			playerNames[2] = bluePlayer
			playerCircles[3] = greenPlayer
		elif playerCount == 4:
			canvasImage.delete(redPlayer)
			canvasImage.delete(yellowPlayer)
			canvasImage.delete(bluePlayer)
			canvasImage.delete(greenPlayer)
			canvasImage.delete(orangePlayer)
			redPlayer = canvasImage.create_oval(inGamePoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
			yellowPlayer = canvasImage.create_oval(inGamePoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
			bluePlayer = canvasImage.create_oval(inGamePoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
			greenPlayer = canvasImage.create_oval(inGamePoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
			orangePlayer = canvasImage.create_oval(waitingPoints[4], outline=colors[4][0], fill=colors[4][1], width=2)
			playerCircles[0] = redPlayer
			playerCircles[1] = yellowPlayer
			playerNames[2] = bluePlayer
			playerCircles[3] = greenPlayer
			playerCircles[4] = orangePlayer
		p1Place = 0
		p2Place = 0
		p3Place = 0
		p4Place = 0
		p5Place = 0
		currPlayer = playerNames[0]

def resBtnFunc():
	global p1Place, p2Place, p3Place, p4Place, p5Place, playerNames, currPlayer, redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, playerCircles
	p1Place = 0
	p2Place = 0
	p3Place = 0
	p4Place = 0
	p5Place = 0
	resSpots()
	currPlayer = playerNames[0]
	return

def resSpots():
	global redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, canvasImage, waitingPoints, playerCount, inGamePoints, maxPlayer
	canvasImage.delete(redPlayer)
	canvasImage.delete(yellowPlayer)
	canvasImage.delete(bluePlayer)
	canvasImage.delete(greenPlayer)
	canvasImage.delete(orangePlayer)
	for x in range(playerCount):
		if x == 0:
			redPlayer = canvasImage.create_oval(inGamePoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
		elif x == 1:
			yellowPlayer = canvasImage.create_oval(inGamePoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
		elif x == 2:
			bluePlayer = canvasImage.create_oval(inGamePoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
		elif x == 3:
			greenPlayer = canvasImage.create_oval(inGamePoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
		elif x == 4:
			orangePlayer = canvasImage.create_oval(inGamePoints[4], outline=colors[4][0], fill=colors[4][1], width=2)
	for x in range(playerCount, maxPlayer):
		if x == 0:
			redPlayer = canvasImage.create_oval(waitingPoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
		elif x == 1:
			yellowPlayer = canvasImage.create_oval(waitingPoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
		elif x == 2:
			bluePlayer = canvasImage.create_oval(waitingPoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
		elif x == 3:
			greenPlayer = canvasImage.create_oval(waitingPoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
		elif x == 4:
			orangePlayer = canvasImage.create_oval(waitingPoints[4], outline=colors[4][0], fill=colors[4][1], width=2)


def movePlayer(player, moveDist):
	global playerCount, playerNames, p1Name, p2Name, p3Name, p4Name, p5Name, maxPlayer, currPlayer, startPoints, \
		colors, playerCircles, redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, p1Place, p2Place, p3Place, p4Place, p5Place, pUptPlace
	# X: 61(1 square right), Y: 51 (1 square down)
	if moveDist <= 0:
		return
	if player == p1Name:
		if (pUptPlace == 10 or pUptPlace == 20 or pUptPlace == 30 or pUptPlace == 40 or pUptPlace == 50 or pUptPlace == 60 or pUptPlace == 70 or pUptPlace == 86 or pUptPlace == 92):
			moveBy(redPlayer, "-y")
		elif (0 < pUptPlace < 10 or 20 < pUptPlace < 30 or 40 < pUptPlace < 50 or 60 < pUptPlace < 70 or 80 < pUptPlace < 86 or 92 < pUptPlace < 98):
			moveBy(redPlayer, "x")
		elif (10 < pUptPlace < 20 or 30 < pUptPlace < 40 or 50 < pUptPlace < 60 or 70 < pUptPlace < 80 or 86 < pUptPlace < 92):
			moveBy(redPlayer, "-x")
		elif (pUptPlace == 80):
			moveBy(redPlayer, "2x-y")
		elif (pUptPlace == 98):
			moveBy(redPlayer, "-2.5x-y")
		elif (pUptPlace == 99):
			moveBy(redPlayer, "-y")
			return
		elif (pUptPlace == 0):
			# put the player icon from 0 to the first spot
			canvasImage.delete(redPlayer)
			redPlayer = canvasImage.create_oval(startPoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
		pUptPlace += 1
		movePlayer(player, moveDist-1)
	elif player == p2Name:
		if (pUptPlace == 10 or pUptPlace == 20 or pUptPlace == 30 or pUptPlace == 40 or pUptPlace == 50 or pUptPlace == 60 or pUptPlace == 70 or pUptPlace == 86 or pUptPlace == 92):
			moveBy(yellowPlayer, "-y")
		elif (0 < pUptPlace < 10 or 20 < pUptPlace < 30 or 40 < pUptPlace < 50 or 60 < pUptPlace < 70 or 80 < pUptPlace < 86 or 92 < pUptPlace < 98):
			moveBy(yellowPlayer, "x")
		elif (10 < pUptPlace < 20 or 30 < pUptPlace < 40 or 50 < pUptPlace < 60 or 70 < pUptPlace < 80 or 86 < pUptPlace < 92):
			moveBy(yellowPlayer, "-x")
		elif (pUptPlace == 80):
			moveBy(yellowPlayer, "2x-y")
		elif (pUptPlace == 98):
			moveBy(yellowPlayer, "-2.5x-y")
		elif (pUptPlace == 99):
			moveBy(yellowPlayer, "-y")
			return
		elif (pUptPlace == 0):
			# put the player icon from 0 to the first spot
			canvasImage.delete(yellowPlayer)
			yellowPlayer = canvasImage.create_oval(startPoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
		pUptPlace += 1
		movePlayer(player, moveDist-1)
	elif player == p3Name:
		if (pUptPlace == 10 or pUptPlace == 20 or pUptPlace == 30 or pUptPlace == 40 or pUptPlace == 50 or pUptPlace == 60 or pUptPlace == 70 or pUptPlace == 86 or pUptPlace == 92):
			moveBy(bluePlayer, "-y")
		elif (0 < pUptPlace < 10 or 20 < pUptPlace < 30 or 40 < pUptPlace < 50 or 60 < pUptPlace < 70 or 80 < pUptPlace < 86 or 92 < pUptPlace < 98):
			moveBy(bluePlayer, "x")
		elif (10 < pUptPlace < 20 or 30 < pUptPlace < 40 or 50 < pUptPlace < 60 or 70 < pUptPlace < 80 or 86 < pUptPlace < 92):
			moveBy(bluePlayer, "-x")
		elif (pUptPlace == 80):
			moveBy(bluePlayer, "2x-y")
		elif (pUptPlace == 98):
			moveBy(bluePlayer, "-2.5x-y")
		elif (pUptPlace == 99):
			moveBy(bluePlayer, "-y")
			return
		elif (pUptPlace == 0):
			# put the player icon from 0 to the first spot
			canvasImage.delete(bluePlayer)
			bluePlayer = canvasImage.create_oval(startPoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
		pUptPlace += 1
		movePlayer(player, moveDist-1)	
	elif player == p4Name:
		if (pUptPlace == 10 or pUptPlace == 20 or pUptPlace == 30 or pUptPlace == 40 or pUptPlace == 50 or pUptPlace == 60 or pUptPlace == 70 or pUptPlace == 86 or pUptPlace == 92):
			moveBy(greenPlayer, "-y")
		elif (0 < pUptPlace < 10 or 20 < pUptPlace < 30 or 40 < pUptPlace < 50 or 60 < pUptPlace < 70 or 80 < pUptPlace < 86 or 92 < pUptPlace < 98):
			moveBy(greenPlayer, "x")
		elif (10 < pUptPlace < 20 or 30 < pUptPlace < 40 or 50 < pUptPlace < 60 or 70 < pUptPlace < 80 or 86 < pUptPlace < 92):
			moveBy(greenPlayer, "-x")
		elif (pUptPlace == 80):
			moveBy(greenPlayer, "2x-y")
		elif (pUptPlace == 98):
			moveBy(greenPlayer, "-2.5x-y")
		elif (pUptPlace == 99):
			moveBy(greenPlayer, "-y")
			return
		elif (pUptPlace == 0):
			# put the player icon from 0 to the first spot
			canvasImage.delete(greenPlayer)
			greenPlayer = canvasImage.create_oval(startPoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
		pUptPlace += 1
		movePlayer(player, moveDist-1)
	elif player == p5Name:
		if (pUptPlace == 10 or pUptPlace == 20 or pUptPlace == 30 or pUptPlace == 40 or pUptPlace == 50 or pUptPlace == 60 or pUptPlace == 70 or pUptPlace == 86 or pUptPlace == 92):
			moveBy(orangePlayer, "-y")
		elif (0 < pUptPlace < 10 or 20 < pUptPlace < 30 or 40 < pUptPlace < 50 or 60 < pUptPlace < 70 or 80 < pUptPlace < 86 or 92 < pUptPlace < 98):
			moveBy(orangePlayer, "x")
		elif (10 < pUptPlace < 20 or 30 < pUptPlace < 40 or 50 < pUptPlace < 60 or 70 < pUptPlace < 80 or 86 < pUptPlace < 92):
			moveBy(orangePlayer, "-x")
		elif (pUptPlace == 80):
			moveBy(orangePlayer, "2x-y")
		elif (pUptPlace == 98):
			moveBy(orangePlayer, "-2.5x-y")
		elif (pUptPlace == 99):
			moveBy(orangePlayer, "-y")
			return
		elif (pUptPlace == 0):
			# put the player icon from 0 to the first spot
			canvasImage.delete(orangePlayer)
			orangePlayer = canvasImage.create_oval(startPoints[4], outline=colors[4][0], fill=colors[4][1], width=2)
		pUptPlace += 1
		movePlayer(player, moveDist-1)
	return

def moveBy(playerCirc, moveRotation):
	global playerCount, playerNames, p1Name, p2Name, p3Name, p4Name, p5Name, maxPlayer, currPlayer, startPoints, \
		colors, playerCircles, redPlayer, yellowPlayer, bluePlayer, greenPlayer, orangePlayer, canvasImage, pUptPlace
	if (playerCirc == redPlayer):
		if (moveRotation == "-y"):
			canvasImage.move(redPlayer, 0, -51)
		elif (moveRotation == "x"):
			canvasImage.move(redPlayer, 61, 0)
		elif (moveRotation == "-x"):
			canvasImage.move(redPlayer, -61, 0)
		elif (moveRotation == "2x-y"):
			canvasImage.move(redPlayer, 122, -51)
		elif (moveRotation == "-2.5x-y"):
			canvasImage.move(redPlayer, -152, -51)
	elif (playerCirc == yellowPlayer):
		if (moveRotation == "-y"):
			canvasImage.move(yellowPlayer, 0, -51)
		elif (moveRotation == "x"):
			canvasImage.move(yellowPlayer, 61, 0)
		elif (moveRotation == "-x"):
			canvasImage.move(yellowPlayer, -61, 0)
		elif (moveRotation == "2x-y"):
			canvasImage.move(yellowPlayer, 122, -51)
		elif (moveRotation == "-2.5x-y"):
			canvasImage.move(yellowPlayer, -152, -51)
	elif (playerCirc == bluePlayer):
		if (moveRotation == "-y"):
			canvasImage.move(bluePlayer, 0, -51)
		elif (moveRotation == "x"):
			canvasImage.move(bluePlayer, 61, 0)
		elif (moveRotation == "-x"):
			canvasImage.move(bluePlayer, -61, 0)
		elif (moveRotation == "2x-y"):
			canvasImage.move(bluePlayer, 122, -51)
		elif (moveRotation == "-2.5x-y"):
			canvasImage.move(bluePlayer, -152, -51)
	elif (playerCirc == greenPlayer):
		if (moveRotation == "-y"):
			canvasImage.move(greenPlayer, 0, -51)
		elif (moveRotation == "x"):
			canvasImage.move(greenPlayer, 61, 0)
		elif (moveRotation == "-x"):
			canvasImage.move(greenPlayer, -61, 0)
		elif (moveRotation == "2x-y"):
			canvasImage.move(greenPlayer, 122, -51)
		elif (moveRotation == "-2.5x-y"):
			canvasImage.move(greenPlayer, -152, -51)
	elif (playerCirc == orangePlayer):
		if (moveRotation == "-y"):
			canvasImage.move(orangePlayer, 0, -51)
		elif (moveRotation == "x"):
			canvasImage.move(orangePlayer, 61, 0)
		elif (moveRotation == "-x"):
			canvasImage.move(orangePlayer, -61, 0)
		elif (moveRotation == "2x-y"):
			canvasImage.move(orangePlayer, 122, -51)
		elif (moveRotation == "-2.5x-y"):
			canvasImage.move(orangePlayer, -152, -51)


buttonNames = ["Restart Game", "Add Player", "Remove Player", "Roll Dice"]
buttonFunctions = [resBtnFunc, addPlayerBtnFunc, removePlayerBtnFunc, rollDiceBtnFunc]

#while (p1Place < endPoint and p2Place < endPoint and p3Place < endPoint):
#	playerTurn(currPlayer)

''' Pygame Option
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sladder")
img = pygame.image.load('./img/snake_and_ladder_map.jpg')
img = pygame.transform.scale(img, (675, 800))
done = False
bg = (127, 127, 127)

while not done:
	for event in pygame.event.get():
		screen.fill(bg)
		rect = img.get_rect()
		rect.center = img.get_rect().center
		screen.blit(img, rect)
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			done = True
	pygame.display.update()
'''

# Create the main window
window = tk.Tk()
window.title("Sladder")
window.geometry("830x800")
window.configure(background='white')

# Create Canvases for image and buttons
canvasImage = Canvas(window, width=675, height=800)
canvasImage.pack(side="left", fill="both", expand=True)
canvasButtons = Canvas(window, width=100, height=800)
canvasButtons.pack(side="right", fill="both", expand=True)

# Add Game Board to the left of the screen
path = "./img/snake_and_ladder_map.jpg"

img = ImageTk.PhotoImage(Image.open(path).resize((675, 800)))

# Add image to the left Canvas
canvasImage.create_image(0,0, anchor=NW, image=img)

'''
# Add Restart Button to the right of the screen
resBtn = tk.Button(canvasButtons, text="Restart Game", height=2, width=20, anchor=W, command= resBtnFunc)
canvasButtons_window = canvasButtons.create_window(0, 0, anchor=NW, window=resBtn)
'''
# Add Buttons and Rolled Dice Label to the Right Canvas
for i in range(len(buttonNames)):
	# Create a Button widget for each button
	button = tk.Button(canvasButtons, text=buttonNames[i], height=2, width=20, anchor=W, command= buttonFunctions[i])
	button.grid(row=i, column=0, padx=10, pady=10)
# Rolled Dice Label
rolledDice = tk.Label(canvasButtons, text="Rolled Dice: " + str(diceRolled), height=2, width=20, anchor=W)
rolledDice.grid(row=len(buttonNames), column=0, padx=10, pady=10)

redPlayer = canvasImage.create_oval(waitingPoints[0], outline=colors[0][0], fill=colors[0][1], width=2)
yellowPlayer = canvasImage.create_oval(waitingPoints[1], outline=colors[1][0], fill=colors[1][1], width=2)
bluePlayer = canvasImage.create_oval(waitingPoints[2], outline=colors[2][0], fill=colors[2][1], width=2)
greenPlayer = canvasImage.create_oval(waitingPoints[3], outline=colors[3][0], fill=colors[3][1], width=2)
orangePlayer = canvasImage.create_oval(waitingPoints[4], outline=colors[4][0], fill=colors[4][1], width=2)


#Start the GUI
window.mainloop()