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
i = 0
playerCount = 0
maxPlayer = 5
playerNames = [p1Name, p2Name, p3Name, p4Name, p5Name]
currPlayer = playerNames[i]
inputtxt = ""
inputFromUser = ""
frame = ""
upperSpots = [[20, 39], [30, 53], [37, 65], [59, 78], [69, 86], [85, 94]]
lowerSpots = [[96, 2], [54, 7], [25, 9], [41, 21], [70, 31], [83, 38], [79, 42], [92, 64]]

def dice():
	global diceRolled, p1Place, p2Place, p3Place, p4Place, p5Place, p1Name, p2Name, p3Name, p4Name, p5Name
	diceRolled = random.choice([1,2,3,4,5,6])
	rolledDice.config(text="Rolled Dice: " + str(diceRolled))
	print(p1Name + ": " + str(p1Place) + ", " + p2Name + ": " + str(p2Place) + ", p3: " + str(p3Place) + ", p4: " + str(p4Place) + ", p5: " + str(p5Place))
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
	global p1Place, p2Place, p3Place, p4Place, p5Place, p1Name, p2Name, p3Name, p4Name, p5Name
	x = checkUpper(place)
	if x < 0:
		x = checkLower(place)
	if x > 0:
		if player == p1Name:
			p1Place = x
		elif player == p2Name:
			p2Place = x
		elif player == p3Name:
			p3Place = x
		elif player == p4Name:
			p4Place = x
		elif player == p5Name:
			p5Place = x

def setPlayers(playerName):
	global playerCount, playerNames, p1Name, p2Name, p3Name, p4Name, p5Name
	if playerCount > maxPlayer:
		playerCount -= 1
		return
	if playerCount == 1:
		p1Name = playerName
		playerNames[0] = p1Name
	elif playerCount == 2:
		p2Name = playerName
		playerNames[1] = p2Name
	elif playerCount == 3:
		p3Name = playerName
		playerNames[2] = p3Name
	elif playerCount == 4:
		p4Name = playerName
		playerNames[3] = p4Name
	elif playerCount == 5:
		p5Name = playerName
		playerNames[4] = p5Name

def playerTurn(player):
	global p1Place, p2Place, p3Place, p4Place, p5Place, p1Name, p2Name, p3Name, p4Name, p5Name
	if player == p1Name:
		p1Place += dice()
		if p1Place >= 100:
			p1Place = 100
			print(p1Name + " is the winner")
			return
		checkSpots(player, p1Place)
	elif player == p2Name:
		p2Place += dice()
		if p2Place >= 100:
			p2Place = 100
			print(p2Name + " is the winner")
			return
		checkSpots(player, p2Place)
	elif player == p3Name:
		p3Place += dice()
		if p3Place >= 100:
			p3Place = 100
			print(p3Name + " is the winner")
			return
		checkSpots(player, p3Place)
	elif player == p4Name:
		p4Place += dice()
		if p4Place >= 100:
			p4Place = 100
			print(p4Name + " is the winner")
			return
		checkSpots(player, p4Place)
	elif player == p5Name:
		p5Place += dice()
		if p5Place >= 100:
			p5Place = 100
			print(p5Name + " is the winner")
			return
		checkSpots(player, p5Place)
	nextPlayerTurn()

def nextPlayerTurn():
	global i, currPlayer, playerCount, playerNames
	i += 1
	if i > playerCount:
		i = 1
	currPlayer = playerNames[i]

def rollDiceBtnFunc():
	global currPlayer
	playerTurn(currPlayer)

def getInput():
	global inputtxt, frame, inputFromUser
	inp = inputtxt.get(1.0, "end-1c")
	inputFromUser = inp
	frame.destroy()
	return

def addPlayerBtnFunc():
	global playerCount, inputtxt, frame
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
	setPlayers(inputFromUser)

def removePlayerBtnFunc():
	global playerCount, currPlayer
	currPlayer = 1
	if playerCount > 0:
		playerCount -= 1

def resBtnFunc():
	global p1Place, p2Place, p3Place, p4Place, p5Place
	p1Place = 0
	p2Place = 0
	p3Place = 0
	p4Place = 0
	p5Place = 0
	return



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
resBtn = tk.Button(window, text="Restart Game", height=1, width=20, command= resBtnFunc)
resBtn.grid(row=0, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

# Add Player
addPlayerBtn = tk.Button(window, text="Add Player", height=1, width=20, command= addPlayerBtnFunc)
addPlayerBtn.grid(row=1, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

# Remove Player
removePlayerBtn = tk.Button(window, text="Remove Player", height=1, width=20, command= removePlayerBtnFunc)
removePlayerBtn.grid(row=2, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

# Roll Dice Button
rollDiceBtn = tk.Button(window, text="Roll Dice", height=1, width=20, command = rollDiceBtnFunc)
rollDiceBtn.grid(row=3, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

#Rolled Dice:
rolledDice = tk.Label(window, text="Rolled Dice: " + str(diceRolled), height=2, width=20)
rolledDice.grid(row=4, column=1, rowspan=1, columnspan=1, padx=0, pady=0)


#Start the GUI
window.mainloop()