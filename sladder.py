import random
''' Pygame Option
import pygame, sys
'''
import tkinter as tk
from PIL import ImageTk, Image


endPoint = 100
p1Place = 0
p2Place = 0
p3Place = 0
p4Place = 0
p5Place = 0
p1Name = "p1"
p2Name = "p2"
p3Name = "p3"
p4Name = "p4"
p5Name = "p5"
diceRolled = 0
i = 1
playerCount = 0
maxPlayer = 5
currPlayer = "p"+ str(i)
upperSpots = [[20, 39], [30, 53], [37, 65], [59, 78], [69, 86], [85, 94]]
lowerSpots = [[96, 2], [54, 7], [25, 9], [41, 21], [70, 31], [83, 38], [79, 42], [92, 64]]

def dice():
	global diceRolled
	diceRolled = random.choice([1,2,3,4,5,6])
	rolledDice.config(text="Rolled Dice: " + str(diceRolled))
	return diceRolled

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

def setPlayers(playerName):
	global playerCount
	if playerCount == maxPlayer:
		return
	playerCount += 1
	if playerCount == 1:
		p1Name = playerName
	elif playerCount == 2:
		p2Name = playerName
	elif playerCount == 3:
		p3Name = playerName
	elif playerCount == 4:
		p4Name = playerName
	elif playerCount == 5:
		p5Name = playerName

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
	global i, currPlayer, playerCount
	i += 1
	if i > playerCount:
		i = 1
	currPlayer = "p" + str(i)

def rollDiceBtnFunc():
	global currPlayer
	playerTurn(currPlayer)

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

# Add Game Board to the left of the screen
path = "./img/snake_and_ladder_map.jpg"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path).resize((675, 800)))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
board = tk.Label(window, image = img)
board.grid(row=0, column=0, rowspan=5, padx=0, pady=0)

# Add Restart Button to the right of the screen
resBtn = tk.Button(window, text="Restart Game", height=1, width=20)
resBtn.grid(row=0, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

# Add Player
addPlayerBtn = tk.Button(window, text="Add Player", height=1, width=20)
addPlayerBtn.grid(row=1, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

# Remove Player
removePlayerBtn = tk.Button(window, text="Remove Player", height=1, width=20)
removePlayerBtn.grid(row=2, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

# Roll Dice Button
rollDiceBtn = tk.Button(window, text="Roll Dice", height=1, width=20, command = rollDiceBtnFunc)
rollDiceBtn.grid(row=3, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

#Rolled Dice:
rolledDice = tk.Label(window, text="Rolled Dice: " + str(diceRolled), height=2, width=20)
rolledDice.grid(row=4, column=1, rowspan=1, columnspan=1, padx=0, pady=0)


#Start the GUI
window.mainloop()