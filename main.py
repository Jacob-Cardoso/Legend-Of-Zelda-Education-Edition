'''
Legend Of Zelda: Education Edition
Jacob Cardoso 
May 02, 2020
This program will run a recreated and modified version of the original Legend Of Zelda Game for the NES. This game however, is focused on education and learning while still having the enjoyable combat and open world like the original.
Code Aspects
Clickable buttons.
Difficulty selector.
Difficulty selector changes enemy and boss difficulty.
Sound effects and music.
Using sprites and sprite groups.
Displaying images in Rects.
Transforming Images.
Sprite image changes via keyboard input.
Tile-based grid. Used to create a specific grid onto the screen with each tile being filled with the programmed image.
Tile collision and tilemap creation in text files.
Mouse movement and mouse clicks.
Classes And Objects.
Enemys and their movement and collision.
Enumerate in for loops.
Startscreen and endscreen.
Leadboard system using the user score and the current time.
If statements, loops, OOP, lists, string manipulation, files.
'''
import pygame # Import Pygame and the other required modules.
import sys
import time
import datetime
import random  

pygame.init() # Initialize Pygame.

displayWidth = 1024 # Set the displayWidth and height.
displayHeight = 768

screen = pygame.display.set_mode((displayWidth, displayHeight)) # Set the screen variable to be the display.

pygame.display.set_caption("Legend Of Zelda: Education Edition") # Set the title of the game window.

WHITE = (255, 255, 255) # Declare the Static Variables for the colours that will be used.
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DUNGEONGROUND = (129, 129, 128)
GROUND = (252, 216, 168)
BUTTONWHITE = (200, 200, 200)

b1x = displayWidth / 2 # Declare the variables for the 3 buttons to be used for playing, restarting and quitting the game.
b1y = displayHeight - 100
b1w = 100
b1h = 50
b2x = 100
b2y = displayHeight  - 200
b2w = 100
b2h = 50
b3x = displayWidth - 200
b3y = displayHeight - 200
b3w = 100
b3h = 50

fontTitle = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 7) # Set render, and create rectangles around the text that will be used on the 3 buttons.

p1Title = fontTitle.render("Play", True, BLACK)
p1Rect = p1Title.get_rect(center=(b1x + b1w / 2, b1y + b1h / 2))

restartTitle = fontTitle.render("Quit", True, BLACK)
restartRect = restartTitle.get_rect(center=(b2x + b2w / 2, b2y + b2h / 2))

quitTitle = fontTitle.render("Restart", True, BLACK)
quitRect = quitTitle.get_rect(center=(b3x + b3w / 2, b3y + b3h / 2))

clock = pygame.time.Clock() # Declare the clock and FPS variables.
FPS = 120

TILESIZE = 32 # Create the TILESIZE, GRIDWIDTH and GRIDHEIGHT variables to make each tile 32 pixels by 32 pixels.
GRIDWIDTH = displayWidth / TILESIZE # Set the GRIDWIDTH to the displayWidth / TILESIZE which will create a specific numnber of tiles depending on the TILESIZE.
GRIDHEIGHT = displayHeight / TILESIZE # Set the GRIDHEIGHT to the displayHEIGHT / TILESIZE which will create a specific numnber of tiles depending on the TILESIZE.

wallImage = "images/rocks.png" # Declare the images for the static tiles, ones that will be drawn and not changed.
treeImage = "images/single_tree.png"
waterImage = "images/water.png"
dungeonWallImage = "images/dungeonRock.png"
cactusImage = "images/cactus.png"
swordImage = "images/sword.png"
deadTreeImage = "images/tree.png"
greenWallImage = "images/rocks3.png"
wallImage2 ="images/rocks2.png"
oldManImage = "images/old_man.png"
fireImage = "images/fire.png"
lockImage = "images/lock.png"
dungeonWallImage2 = "images/dungeonRock2.png"

enemyImage = ["images/enemyLeft.png", "images/enemyRight.png", "images/enemyUp.png", "images/enemyDown.png"] # Declare the enemyImage list which will be indexed to change the image of the enemy depending on the direction they're moving.

boss1Image = ["images/boss1D1.png", "images/boss1D2.png", "images/boss1D3.png"] # Declare the 4 bossImage lists that will be indexed depending on the difficulty the player selects.
boss2Image = ["images/boss2D1.png", "images/boss2D2.png", "images/boss2D3.png"]
boss3Image = ["images/boss3D1.png", "images/boss3D2.png", "images/boss3D3.png"]
boss4Image = ["images/boss4D1.png", "images/boss4D2.png", "images/boss4D3.png"]

boss1DeadImage = "images/boss1DEAD.png" # Set the images to be used when each boss is defeated.
boss2DeadImage = "images/boss2DEAD.png"
boss3DeadImage = "images/boss3DEAD.png"
boss4DeadImage = "images/boss4DEAD.png"

player_sprites = pygame.sprite.Group() # Create all the sprite groups that will contain different sprites that can be interacted with.
walls_sprites = pygame.sprite.Group()
grounds_sprites = pygame.sprite.Group()
misc_sprites = pygame.sprite.Group()
sword_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
boss_sprites = pygame.sprite.Group()

music = pygame.mixer.music.stop() # Set the music variable to the pygame.mixer.music method.
musicPlay = True # Set the musicPlay variable to True and the currentSong to 'Overworld'
currentSong = 'Overworld'

currentRoom = 0 # Set the currentRoom to 0 as the player will spawn in that room.
obtainedSword = False # Declare the variable obtainedSword to False, this changes when the player gets the pencil.
attack = False # Set attack to False and count to 1.
count = 1

class Room: # Create the Room class and create the roomData list.
	def __init__(self): 
		self.roomData = []

	def draw(self):
		global currentRoom # Import the global variables currentRoom, musicPlay and currentSong.
		global musicPlay
		global currentSong
		if musicPlay == True: # Check if musicPlay is true and if so run the code below.
			music = pygame.mixer.music.stop()
			if currentSong == 'Overworld': # If the song is set to Overworld, play the audio file for Overworld on an infitie loop and set musicPlay to false so the song doesn't infinitely restart from the beginning everytime pygame loops.
				music = pygame.mixer.music.load('audio/overworld.ogg')
				pygame.mixer.music.play(-1)
				musicPlay = False
			if currentSong == 'Dungeon': # If the song is set to Dungeon, play the audio file for Dungeon on an infitie loop and set musicPlay to false so the song doesn't infinitely restart from the begening everytime pygame loops.
				music = pygame.mixer.music.load('audio/Dungeon.ogg')
				pygame.mixer.music.play(-1)
				musicPlay = False	
			if currentSong == 'Win': # If the song is set to Win, play the audio file for Win on an infitie loop and set musicPlay to false so the song doesn't infinitely restart from the beginning everytime pygame loops.
				music = pygame.mixer.music.load('audio/Win.ogg')
				pygame.mixer.music.play(1)
				musicPlay = False
			if currentSong == 'Death': # If the song is set to Death, play the audio file for Death on an infitie loop and set musicPlay to false so the song doesn't infinitely restart from the beginning everytime pygame loops.
				music = pygame.mixer.music.load('audio/Death.ogg')
				pygame.mixer.music.play(1)
				musicPlay = False
			if currentSong == 'GameWin': # If the song is set to GameWin, play the audio file for GameWin on an infitie loop and set musicPlay to false so the song doesn't infinitely restart from the beginning everytime pygame loops.
				music = pygame.mixer.music.load('audio/GameWin.ogg')
				pygame.mixer.music.play(-1)
				musicPlay = False
			if currentSong == 'FinalBoss': # If the song is set to FinalBoss, play the audio file for FinalBoss on an infitie loop and set musicPlay to false so the song doesn't infinitely restart from the beginning everytime pygame loops.
				music = pygame.mixer.music.load('audio/FinalBoss.ogg')
				pygame.mixer.music.play(-1)
				musicPlay = False

		if currentRoom == 0: # If the currentRoom variable is set to 0 open the room1.txt file, and clear every sprite group except for the player group. This will ensure when the player switches rooms, the data from the previous rooms sprites will not overwrite the desired sprite data.
			self.file = open('room1.txt', 'r')
			misc_sprites.empty()
			sword_sprites.empty()
			walls_sprites.empty()
			grounds_sprites.empty()
			boss_sprites.empty()
			enemy_sprites.empty()
			currentRoom = -1 # Set the currentRoom to -1 to indicate the room has been drawn once and will repeat the code above.
		if currentRoom == 2: # If the currentRoom is 2 and the player has the pencil open room2.txt, clear the sprite groups, and set currentRoom to the negative of itself.
			if obtainedSword == True:
				self.roomData.clear()
				self.file = open('room2.txt', 'r')
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -2
			else:
				self.file = open('room2alt.txt', 'r') # If the player doesn't have the pencil draw the alternate version of the room with locks on some of the pathways. This limits the user from entering the boss rooms before they have the pencil.
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -2
		if currentRoom == 3: # If the currentRoom is 3 and the player has the pencil open room3.txt, clear the sprite groups, and set currentRoom to the negative of itself.
			if obtainedSword == True:
				self.file = open('room3.txt', 'r')
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -3
			else:
				self.file = open('room3alt.txt', 'r')  # If the player doesn't have the pencil draw the alternate version of the room.
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -3
		if currentRoom == 4: # If the currentRoom is 4 and the player has the pencil open room4.txt, clear the sprite groups, and set currentRoom to the negative of itself.
			if obtainedSword == True:
				self.file = open('room4.txt', 'r')
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -4
			else:
				self.file = open('room4alt.txt', 'r') # If the player doesn't have the pencil draw the alternate version of the room.
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -4 
		if currentRoom == 5:  # If the currentRoom is 5 open room5.txt, clear the sprite groups, and set currentRoom to the negative of itself and set musicPlay to True and set the currentSong to Dungeon. This will play the dungeon song when the room is drawn.
			self.file = open('room5.txt', 'r')
			misc_sprites.empty()
			sword_sprites.empty()
			walls_sprites.empty()
			grounds_sprites.empty()
			boss_sprites.empty()
			enemy_sprites.empty()
			currentRoom = -5
			musicPlay = True
			currentSong = 'Dungeon'
		if currentRoom == 6: # If the currentRoom is 6 open room6.txt, clear the sprite groups, and set currentRoom to the negative of itself and set musicPlay to True and set the currentSong to Dungeon. This will play the dungeon song when the room is drawn.
			self.file = open('room6.txt', 'r')
			misc_sprites.empty()
			sword_sprites.empty()
			walls_sprites.empty()
			grounds_sprites.empty()
			boss_sprites.empty()
			enemy_sprites.empty()
			currentRoom = -6
			musicPlay = True
			currentSong = 'Dungeon'
		if currentRoom == 7: # If the currentRoom is 7, the first 3 bosses are alive and the finalBossStart player variable is true, open the alternate room 7 file, clear the sprite groups and set currentRoom to the negative of itself.
			if (player.boss1Dead == False) and (player.boss2Dead == False) and (player.boss3Dead == False) and (player.finalBossStart == True):
				self.file = open('room7alt.txt', 'r')
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -7
			elif (player.boss1Dead == True) and (player.boss2Dead == True) and (player.boss3Dead == True) and (player.finalBossStart == True):  # If the first 3 bosses are defeated and the finalBossStart player variable is true, open the room 7 file, clear the sprite groups and set currentRoom to the negative of itself.
				self.file = open('room7.txt', 'r')
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -7
			else: # If the other two conditions aren't true open the alternate of room 7, clear the sprite groups and set currentRoom to the negative of itself.
				self.file = open('room7alt.txt', 'r')
				misc_sprites.empty()
				sword_sprites.empty()
				walls_sprites.empty()
				grounds_sprites.empty()
				boss_sprites.empty()
				enemy_sprites.empty()
				currentRoom = -7
			musicPlay = True # Set the song to dungeon so it will play when room 7 is entered.
			currentSong = 'Dungeon'
		if currentRoom == 8: # If the currentRoom is 8 open room8.txt, clear the sprite groups, and set currentRoom to the negative of itself and set musicPlay to True and set the currentSong to FinalBoss. This will play the FinalBoss song when the room is drawn.
			self.file = open('room8.txt', 'r')
			misc_sprites.empty()
			sword_sprites.empty()
			walls_sprites.empty()
			grounds_sprites.empty()
			boss_sprites.empty()
			enemy_sprites.empty()
			currentRoom = -8
			musicPlay = True			
			currentSong = 'FinalBoss'

		for line in self.file: # For each line in self.file (which will be set the file for each room depending on what room the player enters.)
			self.roomData.append(line) # Add each line to the self.RoomData list.
		for row, tiles in enumerate(self.roomData): # For each row and tile in the roomData list, run another for loop for each column and tile in each row and for each tile in tiles. Enumerate is used to keep track of what row the first for loop is on and what column the second for loop is on.
			for col, tile in enumerate(tiles):

				'''
				 If each tile from each column and each row is equal to one of the characters below, call the corresponding class which will fill that tile with an image or colour depending on what the class is written to do.
				 In each room file, there is a 32x24 grid which is the displayWidth / 32 and the displayHeight / 32.
				 Each room file contains characters that make up a 32x24 grid and every different character is set to one of the classes declared below.
				 If the code finds the current tile its on matches on of the characters, it'll call the assigned class therefore filling that specific tile on the players screen with whatever class was called. This is done for walls, floors, objects, enemies and even the bosses.
				 This is how the tile/grid system works. It fills the tile its on with whatever class is being called. The code in each class is set to be an image/texture or colour. Each class has two paramters and x and a y, this is the col and row variables.
				 The col variable is the x and the row variable is the y. Each class uses the given col and row variable as its x and y and draws the image/texture or colour to those values multiplied by the TILESIZE. 
				 Without the multiplication by TILESIZE the tiles wouldn't be drawn to the proper spot on the screen and wouldn't form a grid. This makes each class draw the texture to the specific spot on the grid.
				'''

				if tile == '1':
					Wall(col, row)
				if tile == '.':
					Ground(col, row)
				if tile == '2':
					DungeonWall(col, row)
				if tile == '3':
					DungeonGround(col, row)
				if tile == '4':
					Cactus(col, row)
				if tile == '5':
					Water(col, row)
				if tile == '6':
					LightSteel(col, row)
				if tile == '7':
					DeadTree(col, row)
				if tile == '8':
					Sword(col, row)        
				if tile == '9':
					GreenRock(col, row)
				if tile =='!':
					Fire(col, row)    
				if tile =='@':
					DungeonWall2(col, row)  
				if tile == '&':
					Wall2(col, row) 
				if tile == '#':
					Boss1(col, row)  		
				if tile == '$':
					Boss2(col, row)
				if tile == '%':
					Boss3(col, row)
				if tile == '^':
					FinalBoss(col, row) 
				if tile == '*':
					Lock(col, row)
				if tile == '0':
					OldMan(col, row)  
				if tile == 'S':
					EnemySide(col, row)
				if tile == 'U':
					EnemyUp(col, row)

		self.roomData.clear() # After the room is drawn using the tiles and classes, clear the roomData list so the room will not be redrawn constantly in the loop.

class Wall(pygame.sprite.Sprite): # Create one of the wall classes that will: add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(wallImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Wall2(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(wallImage2)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Ground(pygame.sprite.Sprite): # Create one of the ground classes that will: add the wall to the grounds_sprites group, open one of the images to represent a ground tile, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = grounds_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GROUND)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class DungeonWall(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(dungeonWallImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class DungeonGround(pygame.sprite.Sprite): # Create one of the ground classes that will: add the wall to the grounds_sprites group, open one of the images to represent a ground tile, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = grounds_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DUNGEONGROUND)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Cactus(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(cactusImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Water(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(waterImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class LightSteel(pygame.sprite.Sprite): # Create one of the ground classes that will: add the wall to the grounds_sprites group, use the 172, 172, 172 colour as the sprite "image", set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = grounds_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((172, 172, 172))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class DeadTree(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(deadTreeImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class GreenRock(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(greenWallImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Fire(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(fireImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class DungeonWall2(pygame.sprite.Sprite): # Create one of the wall classes that will: Add the wall to the wall_sprites group, open one of the images to represent a wall, transform it to fit the tilesize, set a rectangle around it, and move it to the specific grid position.
    def __init__(self, x, y):
        self.groups = walls_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(dungeonWallImage2)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Sword(pygame.sprite.Sprite): # Create the sword sprite add it to the sword_sprites group and open the swordImage, then move it to the specific grid position. This sprite is seperate from the others because more code is written that if the player collides with any item in the sword_sprites group.
	def __init__(self, x, y):
		self.groups = sword_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.image.load(swordImage)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

class EnemySide(pygame.sprite.Sprite): # Declare the EnemySide sprite. This enemy will move side to side repeatedly.
	def __init__(self, x, y):
		self.groups = enemy_sprites # Add the sprite to the enemy_sprites group.
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.image.load(enemyImage[0]) # Index the enemyImage list and use the first entry in the list as the image for the enemy.
		self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE)) # Transform the image.
		self.rect = self.image.get_rect() # Put a rect around the image.
		self.rect.center = (displayWidth / 2, displayHeight / 2) # Move the rect to the center of the screen.
		self.x = x 
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.num = random.randint(0, 1) # Set the self.num variable to either 0 or 1 picked randomly. This value will be used in the update method.
		self.dx = 0
		self.dy = 0
		self.hitWall = False # Set self.hitWall to False as the enemy isn't hitting a wall. Set count to 1.
		self.count = 1

	def update(self, player): # Define the update method.
		if (self.dx == 1) or (self.dx == 2) or (self.dx == 3): # If the change in x is 1, 2 or 3 set the sprites image to index 1 of the enemyImage list. This is the moving right image.
			self.image = pygame.image.load(enemyImage[1])
			self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
		else: # Else will assume the enemy is moving left so it will assign the enemy left image to the self.image variable.
			self.image = pygame.image.load(enemyImage[0])
			self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))

		if self.count == 1: # If the self.count variable is 1 move the enemy rect to itself - 33 * TILESIZE.
			
			'''
			This code fixes the only issue with the tile based system.
			The issue occurs with trying to draw a moving sprite to the screen from the text file for the room. When this happens and the enemy moves from its drawn spot a black square is left there and cannot be filled.
			To combat this, for each file that contains an enemy, I doubled the amount of columns in the file. Therefore creating two rooms in one file, one room is the original with the walls, ground sprites and other tiles.
			The other room, to the direct right of the text in the file, contains the enemy tiles. Each enemy is placed exactly where they would be if they were placed in the original room but in the second room that only contains enemies.
			The code below runs once for each enemy. It takes the enemy from it position in the second room which isn't visible to the player. It can only be seen when looking at the layout of the file. And moves the enemy back by 33 * TILESIZE. 
			This means that it takes the enemy from its position in the second room and moves it to where it should be in the first room. Once again, this is done by creating an invisible second room in each file that contains enemies.
			The second room is the exact size of every other room but its made to only contain enemy sprites. When the game reads and draws the room, the enemies are drawn off the screen in the position indicated by the file.
			As soon as each enemy is drawn its moved to its current position minus the exact length of a room which is 33 * TILESIZE. As there are 33 columns in each file. 
			This solves the black square issue by drawing the enemies in the correct position just increased by the length of the room. When they're drawn they're immediatly moved back by the roomsize. Making it look like they were always there.
			'''
			
			self.rect.x -= 33 * TILESIZE
			self.num = random.randint(0, 1) # Randomly pick between 0 and 1. If the number is 0, change the dx by a positiive number depending on the difficulty. This moves the enemy right.
			if self.num == 0:
				if player.difficulty == 1:
					self.dx = 1
				elif player.difficulty == 2:
					self.dx = 2
				elif player.difficulty == 3:
					self.dx = 3
			elif self.num == 1: # If the number is 1 move them to the left by the amount decided by the difficulty.
				if player.difficulty == 1:
					self.dx = -1
				elif player.difficulty == 2:
					self.dx = -2
				elif player.difficulty == 3:
					self.dx = -3			
			self.count = 0
		self.oldx = self.rect.x # Set the enemy position to the oldx and oldy values.
		self.oldy = self.rect.y 
		self.rect.move_ip(self.dx, 0) # Move the enemy.
		self.rect.move_ip(0, self.dy)
		
		for wall in walls_sprites: # For each wall in the walls_sprites group, check if the enemy collides with it and reverse its movement if so.
			if (self.rect.colliderect(wall.rect)) and (self.hitWall == False): 
				self.hitWall = True
				self.dx = -self.dx
				self.dy = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
			else:
				self.hitWall = False

class EnemyUp(pygame.sprite.Sprite): # Declare the EnemyUp sprite. This enemy will move up and down repeatedly.
	def __init__(self, x, y):
		self.groups = enemy_sprites # Add the sprite to the enemy_sprites group.
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.image.load(enemyImage[3]) # Index the enemyImage list and use the 3rd index in the list as the image for the enemy.
		self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE)) # Transform the image.
		self.rect = self.image.get_rect() # Put a rect around the image.
		self.rect.center = (displayWidth / 2, displayHeight / 2) # Move the rect to the center of the screen.
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.num = random.randint(0, 1) # Set the self.num variable to either 0 or 1 picked randomly. This value will be used in the update method.
		self.dx = 0
		self.dy = 0
		self.hitWall = False # Set self.hitWall to False as the enemy isn't hitting a wall. Set count to 1.
		self.count = 1

	def update(self, player): # Define the update method.
		if (self.dy == -1) or (self.dy == -2) or (self.dy == -3): # If the change in y is 1, 2 or 3 set the sprites image to index 2 of the enemyImage list. 
			self.image = pygame.image.load(enemyImage[2])
			self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
		else: # Use enemyImage index 3 as the enemy image if it isn't moving up.
			self.image = pygame.image.load(enemyImage[3])
			self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))

		if self.count == 1: # If the self.count variable is 1 move the enemy rect to itself - 33 * TILESIZE.			
		
			'''
			This code fixes the only issue with the tile based system.
			The issue occurs with trying to draw a moving sprite to the screen from the text file for the room. When this happens and the enemy moves from its drawn spot a black square is left there and cannot be filled.
			To combat this, for each file that contains an enemy, I doubled the amount of columns in the file. Therefore creating two rooms in one file, one room is the original with the walls, ground sprites and other tiles.
			The other room, to the direct right of the text in the file, contains the enemy tiles. Each enemy is placed exactly where they would be if they were placed in the original room but in the second room that only contains enemies.
			The code below runs once for each enemy. It takes the enemy from it position in the second room which isn't visible to the player. It can only be seen when looking at the layout of the file. And moves the enemy back by 33 * TILESIZE. 
			This means that it takes the enemy from its position in the second room and moves it to where it should be in the first room. Once again, this is done by creating an invisible second room in each file that contains enemies.
			The second room is the exact size of every other room but its made to only contain enemy sprites. When the game reads and draws the room, the enemies are drawn off the screen in the position indicated by the file.
			As soon as each enemy is drawn its moved to its current position minus the exact length of a room which is 33 * TILESIZE. As there are 33 columns in each file. 
			This solves the black square issue by drawing the enemies in the correct position just increased by the length of the room. When they're drawn they're immediatly moved back by the roomsize. Making it look like they were always there.
			'''
			
			self.rect.x -= 33 * TILESIZE
			self.num = random.randint(0, 1)
			if self.num == 0:
				if player.difficulty == 1:
					self.dy = 1
				elif player.difficulty == 2:
					self.dy = 2
				elif player.difficulty == 3:
					self.dy = 3
			elif self.num == 1:
				if player.difficulty == 1:
					self.dy = -1
				elif player.difficulty == 2:
					self.dy = -2
				elif player.difficulty == 3:
					self.dy = -3			
			self.count = 0
		
		self.oldx = self.rect.x # Set the enemy position to the oldx and oldy values.
		self.oldy = self.rect.y 
		self.rect.move_ip(self.dx, 0) # Move the enemy.
		self.rect.move_ip(0, self.dy)
		
		for wall in walls_sprites: # For each wall in the walls_sprites group, check if the enemy collides with it and reverse its movement if so.
			if (self.rect.colliderect(wall.rect)) and (self.hitWall == False): 
				self.hitWall = True
				self.dy = -self.dy
				self.dx = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
			else:
				self.hitWall = False

class Boss1(pygame.sprite.Sprite): # Create the Boss1 class.
    def __init__(self, x, y): 
        global boss1DeadImage # Import the boss1DeadImage global variable.
        self.groups = boss_sprites # Add the sprite to the boss_sprites group.
        pygame.sprite.Sprite.__init__(self, self.groups)

        if player.boss1Dead == False: # If the boss isn't defeated depending on the difficulty load the corresponding image from the boss1Image list. Each image contains a different question and the difficulty of those questions will change depending on what difficulty the player selects.
            if player.difficulty == 1:
                self.image = pygame.image.load(boss1Image[0])
            if player.difficulty == 2:
                self.image = pygame.image.load(boss1Image[1])
            if player.difficulty == 3:
                self.image = pygame.image.load(boss1Image[2])
        else: # Else means the player has defeated the boss so load the boss1DeadImage.
            self.image = pygame.image.load(boss1DeadImage) 

        self.rect = self.image.get_rect() # Define the rectangle for the image.
        self.rect.center = (displayWidth / 2, displayHeight / 2) # Center the rect.
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Boss2(pygame.sprite.Sprite): # Create the Boss2 class.
    def __init__(self, x, y):
        global boss2DeadImage # Import the boss2DeadImage global variable.
        self.groups = boss_sprites # Add the sprite to the boss_sprites group.
        pygame.sprite.Sprite.__init__(self, self.groups)

        if player.boss2Dead == False: # If the boss isn't defeated depending on the difficulty load the corresponding image from the boss2Image list. Each image contains a different question and the difficulty of those questions will change depending on what difficulty the player selects.
            if player.difficulty == 1:
                self.image = pygame.image.load(boss2Image[0])
            if player.difficulty == 2:
                self.image = pygame.image.load(boss2Image[1])
            if player.difficulty == 3:
                self.image = pygame.image.load(boss2Image[2])
        else: # Else means the player has defeated the boss so load the boss2DeadImage.
            self.image = pygame.image.load(boss2DeadImage)     

        self.rect = self.image.get_rect()
        self.rect.center = (displayWidth / 2, displayHeight / 2)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Boss3(pygame.sprite.Sprite): # Create the Boss3 class.
    def __init__(self, x, y):
        global boss3DeadImage # Import the boss3DeadImage global variable.
        self.groups = boss_sprites # Add the sprite to the boss_sprites group.
        pygame.sprite.Sprite.__init__(self, self.groups)

        if player.boss3Dead == False: # If the boss isn't defeated depending on the difficulty load the corresponding image from the boss3Image list. Each image contains a different question and the difficulty of those questions will change depending on what difficulty the player selects.
            if player.difficulty == 1:
                self.image = pygame.image.load(boss3Image[0])
            if player.difficulty == 2:
                self.image = pygame.image.load(boss3Image[1])
            if player.difficulty == 3:
                self.image = pygame.image.load(boss3Image[2])
        else: # Else means the player has defeated the boss so load the boss3DeadImage.
            self.image = pygame.image.load(boss3DeadImage)     

        self.rect = self.image.get_rect()
        self.rect.center = (displayWidth / 2, displayHeight / 2)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class FinalBoss(pygame.sprite.Sprite): # Create the FinalBoss class.
    def __init__(self, x, y):
        global boss4DeadImage # Import the boss4DeadImage global variable.
        self.groups = boss_sprites # Add the sprite to the boss_sprites group.
        pygame.sprite.Sprite.__init__(self, self.groups)

        if player.boss4Dead == False: # If the boss isn't defeated depending on the difficulty load the corresponding image from the boss4Image list. Each image contains a different question and the difficulty of those questions will change depending on what difficulty the player selects.
            if player.difficulty == 1:
                self.image = pygame.image.load(boss4Image[0])
            if player.difficulty == 2:
                self.image = pygame.image.load(boss4Image[1])
            if player.difficulty == 3:
                self.image = pygame.image.load(boss4Image[2])
        else: # Else means the player has defeated the boss so load the boss4DeadImage.
            self.image = pygame.image.load(boss4DeadImage) 

        self.rect = self.image.get_rect()
        self.rect.center = (displayWidth / 2, displayHeight / 2)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE 

class OldMan(pygame.sprite.Sprite): # Create the OldMan class, add it to the misc_sprites group, then open the oldManImage, put a rectangle around it then move it to the specific grid location.
    def __init__(self, x, y):
        self.groups = misc_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(oldManImage)
        self.rect = self.image.get_rect()
        self.rect.center = (displayWidth / 2, displayHeight / 2)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Lock(pygame.sprite.Sprite): # Create the Lock class, add it to the misc_sprites group, then open the lockImage, put a rectangle around it then move it to the specific grid location.
    def __init__(self, x, y):
        self.groups = misc_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(lockImage)
        self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Player(pygame.sprite.Sprite): # Create the Player class and initialize it.
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/link_down1.png') # Set the regular image to the player facing down and transform it to fit the TILESIZE.
		self.image =  pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
		self.rect = self.image.get_rect()
		self.rect.center = (displayWidth / 2, displayHeight / 2) # Declare the image rectangle, variables for movement and default difficulty.
		self.dx = 0
		self.dy = 0
		self.speed = 3
		self.difficulty = 1
		self.hitWall = False # Declare the hit variables and set them to False as the player won't be colliding with anything from the start.
		self.hitSword = False
		self.hitMisc = False
		self.hitEnemy = False
		self.hitBoss = False
		self.boss1Dead = False # Declare the bossDead variables, set them to False as each boss is alive by default.
		self.boss2Dead = False
		self.boss3Dead = False
		self.boss4Dead = False
		self.finalBossStart = True # finalBossStart is set to True so when the player enters the final room the boss will start automatically.
		self.score = 0 # Set the score to 0 and default lives to 3.
		self.lives = 3
		self.fontTitle = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 20) # Define, render and put a rectangle around the score and lives font.
		self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 
		self.scoreRect = self.scoreTitle.get_rect(topright=(displayWidth - 70, 35)) 
		self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
		self.lifeRect = self.lifeTitle.get_rect(topleft=(70, 35)) 

	def update(self): # Define the update method.
		global currentRoom # Import the global variables to be used.
		global musicPlay
		global currentSong
		global endLoop

		if self.boss4Dead == True: # Checks if the player wins or loses, set the lives of the player to 100 if they win. This will be used in the EndScreen code.
			self.lives = 100
		if (self.lives == 0) or (self.lives == 100):
			endLoop = True

		self.oldx = self.rect.x # Set the oldx and oldy variables to prevent movement through walls. 
		self.oldy = self.rect.y
		self.rect.move_ip(self.dx, 0) # Move the player by the dx and dy.
		self.rect.move_ip(0, self.dy)

		if (self.rect.top <= 0) and (currentRoom == -1): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 2
			self.rect.x = displayWidth / 2
			self.rect.y = displayHeight - self.rect.height - 5
		if (self.rect.top <= 0) and (currentRoom == -2): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 3
			self.rect.x = displayWidth / 2
			self.rect.y = displayHeight - self.rect.height
		if (self.rect.bottom >= displayHeight) and (currentRoom == -2): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 0
			self.rect.x = displayWidth / 2
			self.rect.y = 0 + self.rect.height
		if (self.rect.bottom >= displayHeight) and (currentRoom == -3): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 2
			self.rect.x = displayWidth / 2
			self.rect.y = 0 + self.rect.height
		if (self.rect.left <= 0) and (currentRoom == -2):
			currentRoom = 4
			self.rect.x = displayWidth - self.rect.width
			self.rect.y = (displayHeight / 2) - TILESIZE
		if (self.rect.right >= displayWidth) and (currentRoom == -4): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 2
			self.rect.x = 0
			self.rect.y = (displayHeight / 2) - TILESIZE
		if (self.rect.top <= 0) and (currentRoom == -4): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 5
			self.rect.x = displayWidth - self.rect.width * 2
			self.rect.y = displayHeight - self.rect.height * 2
		if (self.rect.bottom >= displayHeight) and (currentRoom == -5): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 4
			self.rect.x = displayWidth - (TILESIZE * 8)
			self.rect.y = 0 + self.rect.height 
			musicPlay = True
			currentSong = 'Overworld' # Set the variables neccesary to play the Overworld song.
		if (self.rect.top <= 0) and (currentRoom == -3):
			currentRoom = 6
			self.rect.x = displayWidth / 2
			self.rect.y = displayHeight - self.rect.height
		if (self.rect.bottom >= displayHeight) and (currentRoom == -6): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 3
			self.rect.x = displayWidth / 2
			self.rect.y = 0 + self.rect.height
			musicPlay = True # Set the variables neccesary to play the Overworld song.
			currentSong = 'Overworld'
		if (self.rect.right >= displayWidth) and (currentRoom == -2): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 7
			self.rect.x = 0 + self.rect.width
			self.rect.y = displayHeight / 2
		if (self.rect.left <= 0) and (currentRoom == -7): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 2
			self.rect.x = displayWidth - self.rect.width
			self.rect.y = displayHeight / 2
			musicPlay = True
			currentSong = 'Overworld' # Set the variables neccesary to play the Overworld song.
		if (self.rect.top <= 0) and (currentRoom == -7): # Checks if the player has hit a "loading zone." Set the currentRoom variable to the correct room entered and move the player to the desired starting position for the room.
			currentRoom = 8
			self.rect.x = displayWidth / 2
			self.rect.y = displayHeight - self.rect.height * 2

	def collide_with_walls(self): # Checking player collision with each wall in the walls_sprites group. When each room is drawn the sprite group is filled with each individual wall tile.
		for wall in walls_sprites:
			if (self.rect.colliderect(wall.rect)) and (self.hitWall == False): # If the player rectangle collides with any of the rectangles around any of the walls in the walls_sprites group stop the player from moving and move them back to the oldx and oldy variable.
				self.hitWall = True
				self.dx = 0
				self.dy = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
			else:
				self.hitWall = False

	def collide_with_misc(self): # Checking player collision with each misc sprite in the misc_sprites group. 
		for misc in misc_sprites:
			if (self.rect.colliderect(misc.rect)) and (self.hitMisc == False): # If the player rectangle collides with any of the rectangles around any of the misc sprites in the misc_sprites group stop the player from moving and move them back to the oldx and oldy variable.
				self.hitMisc = True
				self.dx = 0
				self.dy = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
			else:
				self.hitMisc = False

	def collide_with_enemy(self): # Checking player collision with each enemy in the enemy_sprites group.
		global attack
		for enemy in enemy_sprites:
			if (self.rect.colliderect(enemy.rect)) and (self.hitEnemy == False): # If the player rectangle collides with any of the rectangles around any of the enemy sprites in the enemy_sprites group stop the player from moving and move them back to the oldx and oldy variable. Then set the enemy dx and dy to the opposite of what it was previously, switching the direction the enemy is going.
				self.hitEnemy = True
				self.dx = 0
				self.dy = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
				enemy.dx = -enemy.dx
				enemy.dy = -enemy.dy

				if attack == False: # If the player isn't attacking and they collide with an enemy, lower their lives by 1 and render the font with the new lives variable.
					self.lives -= 1
					self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
					self.lifeRect = self.lifeTitle.get_rect(topleft=(70, 35)) 
				if attack == True: # If the player is attacking and they collide with an enemy, increase their score by 1 and render the font with the new score variable, then remove that enemy from the sprites group so they dissapear from the display.
					enemy_sprites.remove(enemy)
					self.score += 1
					self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 
					self.scoreRect = self.scoreTitle.get_rect(topright=(displayWidth - 70, 35)) 
					attack = False
			else: # If the player isn't colliding with an enemy set the hitEnemy variable to False.
				self.hitEnemy = False

	def collide_with_sword(self, room): # Define the collide_with_sword method to check if the player collides with the pencil they have to pickup.
		global obtainedSword # Import the required global variables.
		global currentRoom
		global musicPlay
		global currentSong

		for sword in sword_sprites: # For each sword in sword_sprites check if the player rect collides with the sword rect. If so, stop the player from moving, move them to the oldx and oldy position.
			if (self.rect.colliderect(sword.rect)) and (self.hitSword == False): 
				self.hitSword = True
				self.dx = 0
				self.dy = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
				obtainedSword = True # Set the obtainedSword variable to True as the player now has the pencil to attack with.
				currentRoom = 3 # Set the currentRoom to 3. This will force a redraw of the room with the locks removed and enemys drawn.
				musicPlay = True # Set the variables to play the Win song and change the player image to show they interacted with the pencil.
				currentSong = 'Win'
				self.image = pygame.image.load('images/link_sword.png')
				self.rect.center = (displayWidth / 2, displayHeight / 2) 
			else:
				self.hitSword = False

	def collide_with_boss(self): # Define the collide_with_boss method which checks if the player collides with each boss in the boss_sprites group. If the player collides, stop them from moving and move them to the oldx and oldy position.
		for boss in boss_sprites:
			if (self.rect.colliderect(boss.rect)) and (self.hitBoss == False): 
				self.hitBoss = True
				self.dx = 0
				self.dy = 0
				self.rect.x = self.oldx
				self.rect.y = self.oldy
			else:
				self.hitBoss = False

	def collision(self): # Define the collision method and import the required global variables.
		global musicPlay
		global currentSong 
		global currentRoom
		global attack

		if self.hitSword == True: # If the player collides with the sword stop their movement, sleep the program so it freezes on the player holding the pencil and the text box appearing. 
			self.dx = 0
			self.dy = 0	
			time.sleep(8)
			self.image = pygame.image.load('images/link_down1.png') # Change the player image to the default one, transform the image and move the rect.
			self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
			self.rect.center = (displayWidth / 2, displayHeight / 2 + 100)
			musicPlay = True # Code to restart the Overworld music as the Win sound was previously playing.
			currentSong = 'Overworld'
			self.hitSword = False
		else:
			if event.type == pygame.KEYDOWN: # Movement for the player using WASD and Space for attacking.
				if event.key == pygame.K_w:
					self.dy = -self.speed
					self.image = pygame.image.load('images/link_up1.png') # If the player is moving up change the image to match their movement. This creates the animated images for when the player moves.
					self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
				elif event.key == pygame.K_s:
					self.dy = self.speed
					self.image = pygame.image.load('images/link_down1.png') # If the player is down up change the image to match their movement.
					self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))

				if event.key == pygame.K_a:
					self.dx = -self.speed
					self.image = pygame.image.load('images/link_left1.png') # If the player is left up change the image to match their movement.
					self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
				elif event.key == pygame.K_d:
					self.dx = self.speed
					self.image = pygame.image.load('images/walk_right1.png') # If the player is right up change the image to match their movement.
					self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
				
				if obtainedSword == True: # If the player has obtained the pencil and they hit Space set attack to True. This will allow them to kill enemies and change the player image depending on the direction they are moving.
					if event.key == pygame.K_SPACE:
						attack = True
						if self.dy == 3:
							self.image = pygame.image.load('images/attack_down.png')
						elif self.dy == -3:						
							self.image = pygame.image.load('images/attack_up.png')
						if self.dx == 3:
							self.image = pygame.image.load('images/attack_right.png')
						elif self.dx == -3:						
							self.image = pygame.image.load('images/attack_left.png')
						if self.dx == 0 and self.dy == 0:
							self.image = pygame.image.load('images/attack_down.png')

				'''
				The next section of code is meant to handle the player challenging the bosses.
				Depending on the difficulty of the game and what key is pressed in each room, the players lives or score will increase or decrease.
				The game checks for if the 1, 2 or 3 keys are pressed for each room. If the key they pressed corresponds with the correct answer for that difficulty and room, they'll gain a life and their score will go up by 100. 
				If they press the wrong key for the room they will lose a life.
				Depending on the change in score or lives that text will be re-rendered to the screen with the new values for the lives or score variable. 
				When a player gets the answer correct, besides their lives and score increasing, the bossDead variable for that room is set to True and the currentRoom value is reset so the room is redrawn. When the room is redrawn the boss's image will have changed to indicate the player defeated them.
				''' 
		
				if self.difficulty == 1: 
					if event.key == pygame.K_1:
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives -= 1
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives -= 1
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives += 1
							self.score += 100
							self.boss3Dead = True
							currentRoom = 7
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

					elif event.key == pygame.K_2:
						if currentRoom == -7 and self.boss3Dead == False:	
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives -= 1
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives += 1
							self.score += 100
							self.boss1Dead = True
							currentRoom = 5
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives += 1
							self.score += 100
							self.boss2Dead = True
							currentRoom = 6
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

					elif event.key == pygame.K_3:
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives -= 1
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives -= 1
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives += 1
							self.score += 100
							self.boss4Dead = True
							currentRoom = 8
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

				if self.difficulty == 2:
					if event.key == pygame.K_1:
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives -= 1
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives -= 1
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives -= 1
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 

					elif event.key == pygame.K_2:
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives -= 1
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives -= 1
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives += 1
							self.score += 100
							self.boss4Dead = True
							currentRoom = 8
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

					elif event.key == pygame.K_3:
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives -= 1
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives += 1
							self.score += 100
							self.boss1Dead = True
							currentRoom = 5
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives += 1
							self.score += 100
							self.boss2Dead = True
							currentRoom = 6
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives += 1
							self.score += 100
							self.boss3Dead = True
							currentRoom = 7
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

				if self.difficulty == 3:
					if event.key == pygame.K_1:
						if currentRoom == -7 and self.boss3Dead == False:							
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:							
							self.lives -= 1
						if currentRoom == -5 and self.boss1Dead == False:							
							self.lives += 1
							self.score += 100
							self.boss1Dead = True
							currentRoom = 5
						if currentRoom == -6 and self.boss2Dead == False:							
							self.lives += 1
							self.score += 100
							self.boss2Dead = True
							currentRoom = 6
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

					elif event.key == pygame.K_2:
						if currentRoom == -5 and self.boss1Dead == False:	
							self.lives -= 1
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives -= 1
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:	
							self.lives += 1
							self.score += 100
							self.boss4Dead = True
							currentRoom = 8
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

					elif event.key == pygame.K_3:
						if currentRoom == -5 and self.boss1Dead == False:
							self.lives -= 1
						if currentRoom == -6 and self.boss2Dead == False:
							self.lives -= 1
						if currentRoom == -8 and self.boss4Dead == False:
							self.lives -= 1
						if currentRoom == -7 and self.boss3Dead == False:
							self.lives += 1
							self.score += 100
							self.boss3Dead = True
							currentRoom = 7
						self.lifeTitle = self.fontTitle.render("Lives: " + str(self.lives), True, GREEN) 
						self.scoreTitle = self.fontTitle.render("Score: " + str(self.score), True, WHITE) 

			if event.type == pygame.KEYUP: # If the player lets go of a key stop them from moving and reset their image to the defeault of the player facing down.
				if event.key == pygame.K_w or event.key == pygame.K_s:
					self.dy = 0
					self.image = pygame.image.load('images/link_down1.png')
					self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
				
				if event.key == pygame.K_a or event.key == pygame.K_d:
					self.dx = 0
					self.image = pygame.image.load('images/link_down1.png')
					self.image = pygame.transform.scale(self.image,(TILESIZE, TILESIZE))
				
				if event.key == pygame.K_SPACE: # If the player lets go of the Space key set attack to False so they cannot kill enemies just by colliding with them.
					attack = False

	def draw(self, surf): # Define the draw method to draw the score and lives to the screen. By default the sprites and sprite groups don't need their own draw methods but having one is neccesary in situations where the variables do not directly interact with the player object itself. In this case the text.
		screen.blit(self.scoreTitle, self.scoreRect)
		screen.blit(self.lifeTitle, self.lifeRect)

class StartScreen: # Create the StartScreen class.
	def __init__(self): # Initialize the StartScreen class and import the required global variables.
		global music 
		music = pygame.mixer.music.stop() # When the StartScreen is run, play the Title song on an infinite loop.
		music = pygame.mixer.music.load('audio/Title.ogg')
		pygame.mixer.music.play(-1)		
		screen.fill(BLACK)
		
		self.fontTitle = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 15) # Create and render the text used for the difficulty selector at the bottom of the start screen.
		self.textTitle = self.fontTitle.render("Select A Difficulty: 1 For Easy / 2 For Medium / 3 For Hard", True, WHITE) 
		self.textRect = self.textTitle.get_rect(center=(displayWidth / 2, displayHeight - 15)) 

		self.backgroundImage = pygame.image.load("images/background.png") # Load and put a rect around the background image, and startScreen image which is the main logo for the screen.
		self.backgroundRect = self.backgroundImage.get_rect()
		self.backgroundRect.center = (displayWidth / 2 + 40, displayHeight / 2)
		self.background2Image = pygame.image.load("images/startScreen.png")
		self.background2Image = pygame.transform.scale(self.background2Image,(displayWidth, displayHeight))
		self.background2Rect = self.background2Image.get_rect()
		self.background2Rect.center = (displayWidth / 2, displayHeight / 2) # Centre the main logo.
		
		self.moveImage = pygame.image.load("images/walk_right1.png") # Set the player animation image and rect.
		self.moveImageRect = self.moveImage.get_rect()
		
		self.operatorImage = pygame.image.load("images/operators.png") # Set and transform the operators image to be displayed at the top of the start screen.
		self.operatorImage = pygame.transform.scale(self.operatorImage, (400, 400))
		self.operatorImageRect = self.operatorImage.get_rect()

		self.dx = 3 # Declare the variables for the player animation to move around the screen.
		self.dy = 0
		self.moveImageRect.x = 85
		self.moveImageRect.y = 85

		self.operatorImageRect.x = displayWidth / 2 - (self.operatorImageRect.width / 2 - 40)
		self.operatorImageRect.y = -100

	def update(self): # Update method to move the player animation around the screen. If it collides with the walls change the direction of movement to keep it moving clockwise infinitely.
		if self.moveImageRect.right >= displayWidth - 84:
			self.dy = 3
			self.dx = 0
			self.moveImage = pygame.image.load("images/link_down1.png")
		if self.moveImageRect.left <= 84:
			self.dy = -3
			self.dx = 0
			self.moveImageRect.left = 85
			self.moveImage = pygame.image.load("images/link_up1.png")
		if self.moveImageRect.top <= 84:
			self.dy = 0
			self.dx = 3
			self.moveImageRect.top = 85
			self.moveImage = pygame.image.load("images/walk_right1.png")
		elif self.moveImageRect.bottom >= displayHeight:
			self.dx = -3
			self.dy = 0
			self.moveImageRect.bottom = displayHeight - 1
			self.moveImage = pygame.image.load("images/link_left1.png")
		
		self.moveImageRect.move_ip(self.dx, self.dy) # Move the player animation by the dx and dy values.

	def collision(self, player): # Check for the 1, 2 and 3 keys being pressed.
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1: # If the 1 key is pressed, set the game difficulty to 1 (easy) and render the font to display the player has selected that difficulty.
				player.difficulty = 1
				self.textTitle = self.fontTitle.render("Easy Mode Selected", True, WHITE) 	
				self.textRect = self.textTitle.get_rect(center=(displayWidth / 2 + 35, displayHeight - 15)) 				
			elif event.key == pygame.K_2: # If the 2 key is pressed, set the game difficulty to 2 (medium) and render the font to display the player has selected that difficulty.
				player.difficulty = 2
				self.textTitle = self.fontTitle.render("Medium Mode Selected", True, WHITE) 	
				self.textRect = self.textTitle.get_rect(center=(displayWidth / 2 + 35, displayHeight - 15)) 	
			elif event.key == pygame.K_3: # If the 3 key is pressed, set the game difficulty to 3 (hard) and render the font to display the player has selected that difficulty.
				player.difficulty = 3
				self.textTitle = self.fontTitle.render("Hard Mode Selected", True, WHITE) 	
				self.textRect = self.textTitle.get_rect(center=(displayWidth / 2 + 35, displayHeight - 15)) 	

	def restart(self, player): # Define the restart method to be used when the player restarts the game via the Restart button.
		global music # Import the global variables to be used.
		global currentRoom
		global obtainedSword
		global attack
		global count

		music = pygame.mixer.music.stop() # Play the Title screen song on an infinite loop and fill the screen.
		music = pygame.mixer.music.load('audio/Title.ogg')
		pygame.mixer.music.play(-1)		
		screen.fill(BLACK)

		'''
		Reset all of the start screen variables, including text, images and the player animation.
		'''

		self.fontTitle = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 15) 
		self.textTitle = self.fontTitle.render("Select A Difficulty: 1 For Easy / 2 For Medium / 3 For Hard", True, WHITE) 
		self.textRect = self.textTitle.get_rect(center=(displayWidth / 2, displayHeight - 15)) 
		self.backgroundImage = pygame.image.load("images/background.png")
		self.backgroundRect = self.backgroundImage.get_rect()
		self.backgroundRect.center = (displayWidth / 2 + 40, displayHeight / 2)
		self.background2Image = pygame.image.load("images/startScreen.png")
		self.background2Image = pygame.transform.scale(self.background2Image,(displayWidth, displayHeight))
		self.background2Rect = self.background2Image.get_rect()
		self.background2Rect.center = (displayWidth / 2, displayHeight / 2)
		self.moveImage = pygame.image.load("images/walk_right1.png")
		self.moveImageRect = self.moveImage.get_rect()
		self.operatorImage = pygame.image.load("images/operators.png")
		self.operatorImage = pygame.transform.scale(self.operatorImage, (400, 400))
		self.operatorImageRect = self.operatorImage.get_rect()
		self.dx = 3
		self.dy = 0
		self.moveImageRect.x = 85
		self.moveImageRect.y = 85
		self.operatorImageRect.x = displayWidth / 2 - (self.operatorImageRect.width / 2 - 40)
		self.operatorImageRect.y = -100

		# Reset the global variables.
		currentRoom = 0
		obtainedSword = False
		attack = False

		'''
		Reset all of the Player class variables to their default ones including the images, text, score, lives and the player itself.
		'''

		player.image = pygame.image.load('images/link_down1.png')
		player.image =  pygame.transform.scale(player.image,(TILESIZE, TILESIZE))
		player.rect = player.image.get_rect()
		player.rect.center = (displayWidth / 2, displayHeight / 2)
		player.dx = 0
		player.dy = 0
		player.speed = 3
		player.difficulty = 1
		player.hitWall = False
		player.hitSword = False
		player.hitMisc = False
		player.hitEnemy = False
		player.hitBoss = False
		player.boss1Dead = False
		player.boss2Dead = False
		player.boss3Dead = False
		player.boss4Dead = False
		player.finalBossStart = True
		player.score = 0
		player.lives = 3
		player.fontTitle = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 20) 
		player.scoreTitle = player.fontTitle.render("Score: " + str(player.score), True, WHITE) 
		player.scoreRect = player.scoreTitle.get_rect(topright=(displayWidth - 70, 35)) 
		player.lifeTitle = player.fontTitle.render("Lives: " + str(player.lives), True, GREEN) 
		player.lifeRect = player.lifeTitle.get_rect(topleft=(70, 35)) 

		# Empty all of the sprite groups and reset the global count variable to 1.
		misc_sprites.empty()
		sword_sprites.empty()
		walls_sprites.empty()
		grounds_sprites.empty()
		boss_sprites.empty()
		enemy_sprites.empty()

		count = 1
		
		'''
		Reset all of the EndScreen variables including, text, lists, and the flow control variables that determine writing and reading from the score and player name files.
		'''
		
		endgame.gameWinTitle = endgame.fontTitle.render("You Graduated!", True, GREEN)
		endgame.gameOverTitle = endgame.fontTitle.render("You Failed To Graduate!", True, RED)
		endgame.gameWinRect = endgame.gameWinTitle.get_rect(center=(displayWidth / 2, 50)) 
		endgame.gameOverRect = endgame.gameOverTitle.get_rect(center=(displayWidth / 2, 50)) 
		endgame.current_time = datetime.datetime.now()  
		endgame.playerList = []
		endgame.scoreList = []
		endgame.leaderboardWrite = False
		endgame.scoreWrite = True
		endgame.scoreWrite2 = True
		endgame.playerWrite = True
		endgame.playerWrite2 = True
		endgame.playerY = displayHeight / 2 - 125
		endgame.scoreY = displayHeight / 2 - 125
		endgame.count = 1

	def draw(self, surf): # Draw the start screen images and text.
		screen.blit(self.background2Image, (self.background2Rect)) 
		screen.blit(self.backgroundImage, (self.backgroundRect)) 
		screen.blit(self.moveImage, self.moveImageRect)
		screen.blit(self.operatorImage, self.operatorImageRect)
		screen.blit(self.textTitle, self.textRect) 

class EndScreen:
	def __init__(self): 
		self.fontTitle = pygame.font.SysFont("arial", 80) 
		self.fontSmallTitle = pygame.font.SysFont("arial", 50) 
		self.fontMiniTitle = pygame.font.SysFont("arial", 20) 

		self.gameWinTitle = self.fontTitle.render("You Graduated!", True, GREEN)
		self.gameOverTitle = self.fontTitle.render("You Failed To Graduate!", True, RED)
		self.gameWinRect = self.gameWinTitle.get_rect(center=(displayWidth / 2, 50)) 
		self.gameOverRect = self.gameOverTitle.get_rect(center=(displayWidth / 2, 50)) 
		
		self.current_time = datetime.datetime.now()  
		self.playerList = []
		self.scoreList = []
		self.leaderboardWrite = False
		self.scoreWrite = True
		self.scoreWrite2 = True
		self.playerWrite = True
		self.playerWrite2 = True

		self.playerY = displayHeight / 2 - 125
		self.scoreY = displayHeight / 2 - 125
		
		self.count = 1
		
	def update(self, player):
		global musicPlay
		global currentSong
		
		if player.lives == 0:
			musicPlay = True
			currentSong = "Death"
			player.lives = -1
		if player.lives == 100:
			musicPlay = True
			currentSong =  "GameWin"
			player.lives = -2

	def draw(self, player):
		if player.lives == -1:
			screen.blit(self.gameOverTitle, self.gameOverRect)
			pygame.draw.rect(screen, WHITE, (displayWidth / 2 - 200, displayHeight / 2 - 250, 400, displayHeight))
		if player.lives == -2:
			screen.blit(self.gameWinTitle, self.gameWinRect)
			pygame.draw.rect(screen, WHITE, (displayWidth / 2 - 200, displayHeight / 2 - 250, 400, displayHeight))
		
		if self.count == 1:
			self.leaderboardTitle = self.fontSmallTitle.render("Leaderboard", True, BLACK)
			self.leaderboardRect = self.leaderboardTitle.get_rect(center=(displayWidth / 2, displayHeight / 2 - 225))
			self.scoreTitle = self.fontSmallTitle.render("Your Score: " + str(player.score), True, BLACK)
			self.scoreRect = self.scoreTitle.get_rect(center=(displayWidth / 2, displayHeight / 2 - 175))		
			
			screen.blit(self.leaderboardTitle, self.leaderboardRect)
			screen.blit(self.scoreTitle, self.scoreRect)

			self.count = 0
			player.lives = -100		
		
		if self.leaderboardWrite == True:
			self.playerFile = open('playerName.txt', 'r+')
			self.scoreFile = open('playerScore.txt', 'r+')

			if self.scoreWrite == True:
				self.scoreFile.write(str(player.score) + '\n')
				self.scoreWrite = False
		
			if self.scoreWrite2 == True:
				for line in self.scoreFile:
					line = line[:-1]
					self.scoreList.append(line)
				for val in self.scoreList:
					self.playerScoreText = self.fontMiniTitle.render(val, True, RED)
					self.playerScoreRect = self.playerScoreText.get_rect(center=(displayWidth / 2 + 160, self.scoreY)) 
					screen.blit(self.playerScoreText, self.playerScoreRect)
					self.scoreY += 25
				self.scoreWrite2 = False

			if self.playerWrite == True:
				self.playerFile.write(str(self.current_time) + '\n')
				self.playerWrite = False
			
			if self.playerWrite2 == True:
				for line in self.playerFile:
					line = line[:-1]
					self.playerList.append(line)
				for val in self.playerList:
					self.playerScoreText = self.fontMiniTitle.render(val + '............', True, RED)
					self.playerScoreRect = self.playerScoreText.get_rect(center=(displayWidth / 2 - 15, self.playerY)) 
					screen.blit(self.playerScoreText, self.playerScoreRect)
					self.playerY += 25
				
				self.playerWrite2 = False

			self.scoreFile.close()
			self.playerFile.close()
			self.leaderboardWrite = False			
		
		self.leaderboardWrite = True
		
start = StartScreen() # Set the start and endgame variables to the StartScreen and EndScreen classes respectively.
endgame = EndScreen()

player = Player() # Set the player variable to the Player class.
player_sprites.add(player) # Add the player class to the player_sprites group.

room = Room() # Set the room variable to the Room class.

startLoop = True # Set the startloop to True and the game and endloop to False.
game1p = False
endLoop = False

while startLoop: # Run the while loop for the start screen and check if the player quits the game.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			startLoop = False
		start.collision(player) # Check for keyboard input on the start screen.

	screen.fill(BLACK) # Fill the screen black.
	start.update() # Update the start screen.
	start.draw(screen) # Draw the start screen.
 
	mouse = pygame.mouse.get_pos() # Set the mouse and click variables to the mouse position and what mouse button was clicked.
	click = pygame.mouse.get_pressed()

	if b1x+b1w > mouse[0] > b1x and b1y+b1h > mouse[1] > b1y: # Check if the mouse is hovering over the play button and change the colour of the button if it is.
		pygame.draw.rect(screen, BUTTONWHITE, (b1x,b1y,b1w,b1h))
		if click[0] == 1: # If the player left clicks the button, start the game loop and play the overworld song.
			game1p = True
			musicPlay = True
			currentSong = "Overworld"
	else:
		pygame.draw.rect(screen, WHITE, (b1x,b1y,b1w,b1h))

	screen.blit(p1Title, p1Rect) # Draw the button text and rectangle.

	pygame.display.update() # Update the display.
	clock.tick(FPS) # Tick the clock by FPS.

	while game1p: # While the game loop is running.
		for event in pygame.event.get(): # Check if the player quits the game and exit all the loops if they do.
			if event.type == pygame.QUIT:
				game1p = False	
				startLoop = False	
				endLoop =  False
			player.collision() # Check the player collision from the keyboard inputs.

		room.draw() # Call the draw function from the Room class to draw the room the player is in.

		player.collide_with_walls() # Check if the player collides with any of the sprites in the sprite groups.
		player.collide_with_sword(room)
		player.collide_with_misc()
		player.collide_with_boss()
		player.collide_with_enemy()

		enemy_sprites.update(player) # Update all the enemys in the enemy_sprites group.
		player_sprites.update() # Update the player_sprites group with the player in it.

		screen.fill(BLACK) # Fill the screen black.

		walls_sprites.draw(screen) # Draw all the walls, grounds, misc, sword, bosses and enemy sprites in each of their sprite groups.
		grounds_sprites.draw(screen)
		misc_sprites.draw(screen)
		sword_sprites.draw(screen)
		boss_sprites.draw(screen)
		enemy_sprites.draw(screen)
		
		player_sprites.draw(screen) # Draw the player in the player_sprites group. This comes standard with any sprite group, not to be confused with the draw method for the player class. This draw method only draws the variables that directly affect the player itself, including it's images, movement and collision.

		player.draw(screen) # Call the draw function in the player class. Unlike drawing the entire sprite group like the player_sprites.draw() method, this is only for the player class and seperate from the other method.

		pygame.display.update() # Update the display.

		if player.boss4Dead == True: # If the final boss is defeated sleep the program for 7 seconds so the player can read the final bosses message.
			time.sleep(7)

		clock.tick(FPS) # Tick the clock by FPS.

		while endLoop: # While in the endLoop check if the player quits the game.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					startLoop = False
					endLoop = False
					game1p = False
			if count == 1: # If the count variable is 1, fill the screen black. This only runs once to prevent the game from looping over the values in the player score and name files and overwriting them.
				screen.fill(BLACK)
				count = 0

			room.draw() # Call the draw method for the room class.
			
			endgame.update(player) # Call the update and draw methods for the end screen.
			endgame.draw(player)

			mouse = pygame.mouse.get_pos() # Set the mouse and click variables to the mouse position and what mouse button was clicked.
			click = pygame.mouse.get_pressed()

			if b2x+b2w > mouse[0] > b2x and b2y+b2h > mouse[1] > b2y: # Check if the mouse is hovering over the quit button and change the colour of the button if it is.
				pygame.draw.rect(screen, BUTTONWHITE, (b2x,b2y,b2w,b2h))
				if click[0] == 1: # If the player left clicks the button, quit pygame. 
					pygame.quit()
					sys.exit()
			else:
				pygame.draw.rect(screen, WHITE, (b2x,b2y,b2w,b2h))
			
			if b3x+b3w > mouse[0] > b3x and b3y+b3h > mouse[1] > b3y: # Check if the mouse is hovering over the restart button and change the colour of the button if it is.
				pygame.draw.rect(screen, BUTTONWHITE, (b3x,b3y,b3w,b3h))
				if click[0] == 1: # If the player left clicks the button, exit the endloop and gameloop, and call the restart method from the start screen class. 
					endLoop = False
					game1p = False	
					start.restart(player)
			else:
				pygame.draw.rect(screen, WHITE, (b3x,b3y,b3w,b3h))
			
			screen.blit(restartTitle, restartRect) # Draw the text and textRects for the buttons.
			screen.blit(quitTitle, quitRect)

			pygame.display.update() # Update the display.
			clock.tick(FPS) # Tick the clock by FPS.

pygame.quit() # Quit pygame.
sys.exit()