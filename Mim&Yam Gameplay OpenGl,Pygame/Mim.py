"""
Program name: Mim&Yam Game.py
Objective: Let Mim or Yam gather the candies and goes to each other.

comments: There are only 3 levels in the game till now.

Tested on: Python 3.5
Author:    Mahmoud Youssef & Mahmoud Essam
"""


""" Import all OpenGl libraries and Pygame for textures and sounds. """
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame import *
from math import *
from time import *

""" Variables initialization. """

StartingBackground = None           # Starting Background before starting the game
UpperElement1 = None                # Upper Elements for Level 1 only
StartingBackground2 = None          # Level 2 Background game
StartingBackground3 = None          # Level 3 Background game
GameLogo = None                     # Game Logo
MimChar = None                      # Mim Character
YamChar = None                      # Yam Character
CandyElement = None                 # Candy photo
WinningGame1 = None                 # Winning Level 1
WinningGame2 = None                 # Winning Level 2
WinningGame3 = None                 # Winning Level 3
StartingSound = None                # Level 1 Sound Play
StartingSound2 = None               # Level 2 Sound Play
StartingSound3 = None               # Level 3 Sound Play
CandySound = None                   # Picking a candy sound
DeathSound = None                   # Death Sound
WinningSound = None                 # Winning Sound

# 4 Candy Elements photos.
Candy1 = 0
Candy2 = 0
Candy3 = 0
Candy4 = 0
# Visible Background to remove it when the user Press "S".
VisibleBackground = 0
# Score and Death from level 1 to 3.
Score0 = 0
Score1 = 0
Score2 = 0
Death0 = 0
Death1 = 0
Death2 = 0
# an array that has all images used in the game.
imageSrc = [StartingBackground, UpperElement1, GameLogo, MimChar, YamChar, CandyElement, WinningGame1, StartingBackground2, WinningGame2, StartingBackground3, WinningGame3]
# an array that controls when these sources 're visible.
visibleSrc = [Candy1, Candy2, Candy3, Candy4, VisibleBackground]
# an array that has all sounds used in the game.
audioSrc = [StartingSound, CandySound, DeathSound, WinningSound, StartingSound2, StartingSound3]
# Spheres Drawing for Level 1 , y coordinates
Spheres = [25, -25, 125, -125]
# Spheres Drawing for Level 2
Spheres2 = [-205, -105, -5, 95, 195, -155, -55, 45, 145]
# two arrays that have all scores and death calculated during the game.
Score = [Score0, Score1, Score2]
Death = [Death0, Death1, Death2]

WINDOW_WIDTH = 800      # Window Width 800px
WINDOW_HEIGHT = 600     # Window Height 600px
clr = 0                 # Drawing the ground color
keyboard_x = -255       # Initial Position for level 1 "Mim Char"
keyboard_y = 25         # Initial Position for level 1 "Mim Char"
dix = 1                 # Controls the movement of the spheres in Level 1
diy1 = 1                # Controls the movement of the spheres in Level 2 in y axis ( Up Spheres )
diy2 = 1                # Controls the movement of the spheres in Level 2 in y axis ( Down Spheres )
left = 200              # Initial Position for Spheres in level 1
up = 125                # Initial Position for Up Spheres in Level 2
down = -125             # Initial Position for Down Spheres in Level 2
Level = 0               # Variable that controls going into other levels
PlaySound = 0           # Variable that controls sound on and off

xo = [0, 0, 0, 50, 100, 150, 0, 0, 0, -50, -100, -150]  # Initial Position for Spheres in level 3
yo = [50, 100, 150, 0, 0, 0, -50, -100, -150, 0, 0, 0]  # Initial Position for Spheres in level 3
xn = 0
yn = 0
angle = 0.007                                           # Rotating Angle for level 3


""" This class is responsible for generating the images in the game. """

class SpriteRenderer:
    def __init__(self, sprite_name):

        """
        :param sprite_name: the name of the sprite
        """


        drawings_path = 'C:\\Users\\mr_ho\\Desktop\\mimqq\\Mim&Yam Gameplay'
        self.sprite_path = drawings_path + '\\' + sprite_name

        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()

        self.sprite_data = pygame.image.tostring(self.sprite, "RGBA", 1)
        self.sprite_text_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.sprite_width, self.sprite_height, 0,
        GL_RGBA, GL_UNSIGNED_BYTE, self.sprite_data)

    def render(self, mul=1, brightness=1):

        """
            render the sprite at the origin.
        """

        glEnable(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)

        rx = self.sprite_width
        ry = self.sprite_height

        glColor3f(1 * brightness, 1 * brightness, 1 * brightness)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-1 * rx, -1 * ry, 0)

        glTexCoord2f(0, mul)
        glVertex3f(-1 * rx, 1 * ry, 0)

        glTexCoord2f(mul, mul)
        glVertex3f(1 * rx, 1 * ry, 0)

        glTexCoord2f(mul, 0)
        glVertex3f(1 * rx, -1 * ry, 0)
        glEnd()

        glDisable(GL_TEXTURE_2D)


""" This is our init function. """

def init():
    global imageSrc, audioSrc, PlaySound

    # Loading images and waiting for rendering.
    imageSrc[0] = SpriteRenderer('StartingBackground.png')
    imageSrc[1] = SpriteRenderer('UpperElement1.png')
    imageSrc[2] = SpriteRenderer('GameLogo.png')
    imageSrc[3] = SpriteRenderer('MimChar.png')
    imageSrc[4] = SpriteRenderer('YamChar.png')
    imageSrc[5] = SpriteRenderer('CandyElement.png')
    imageSrc[6] = SpriteRenderer('WinningGame1.png')
    imageSrc[7] = SpriteRenderer('StartingBackground2.png')
    imageSrc[8] = SpriteRenderer('WinningGame2.png')
    imageSrc[9] = SpriteRenderer('StartingBackground3.png')
    imageSrc[10] = SpriteRenderer('WinningGame3.png')


    glClearColor(1.0, 0.95, 0.71, 0.0)      # Color for level 1 background.


    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -300, 300, 0, 100)  # l,r,b,t,n,f
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Initializing pygame mixer and loading sounds and waiting to be played.
    # Sounds must be in WAV Compression.
    pygame.mixer.init()
    audioSrc[0] = pygame.mixer.Sound("StartingNew.wav")
    audioSrc[1] = pygame.mixer.Sound("Candy.wav")
    audioSrc[2] = pygame.mixer.Sound("Death1.wav")
    audioSrc[3] = pygame.mixer.Sound("Winning.wav")
    audioSrc[4] = pygame.mixer.Sound("StartingNew2.wav")
    audioSrc[5] = pygame.mixer.Sound("StartingNew3.wav")

""" This Function is responsible for drawing the Start & End Squares. """

def DrawStart_End():
    global Level
    glLoadIdentity()
    # Drawing 1st Level Start and End Square.
    if Level == 1 :
        glColor(220.0/255, 57.0/255, 62.0/255)
        glBegin(GL_QUADS)
        glVertex2d(-325,50)
        glVertex2d(-325,-50)
        glVertex2d(-225,-50)
        glVertex2d(-225,50)
        glEnd()
        glColor(220.0/255, 57.0/255, 62.0/255)
        glBegin(GL_QUADS)
        glVertex2d(225,50)
        glVertex2d(325,50)
        glVertex2d(325,-50)
        glVertex2d(225,-50)
        glEnd()
    # Drawing 1st Level Start and End Square.
    elif Level == 2 :
        glColor(220.0/255, 57.0/255, 62.0/255)
        glBegin(GL_QUADS)
        glVertex2d(-325,50)
        glVertex2d(-325,-50)
        glVertex2d(-225,-50)
        glVertex2d(-225,50)
        glEnd()
        glColor(220.0/255, 57.0/255, 62.0/255)
        glBegin(GL_QUADS)
        glVertex2d(225,50)
        glVertex2d(325,50)
        glVertex2d(325,-50)
        glVertex2d(225,-50)
        glEnd()
    # Drawing 1st Level Start and End Square.
    elif Level == 3:
        glLoadIdentity()

        glColor(0, 1, 1)
        glBegin(GL_QUADS)
        glVertex2d(-275,25)
        glVertex2d(-275,-25)
        glVertex2d(-175,-25)
        glVertex2d(-175,25)
        glEnd()
        glColor(0, 1, 1)
        glBegin(GL_QUADS)
        glVertex2d(175,25)
        glVertex2d(275,25)
        glVertex2d(275,-25)
        glVertex2d(175,-25)
        glEnd()

""" This Function is responsible for drawing the ground. """

def DrawGround():
    glLoadIdentity()
    global clr, Level
    # Drawing Level 1 Ground.
    if Level == 1:
        for j in range(150, -150, -50):
            for i in range (-225,225,50):
                if(clr % 2 == 1):
                    glColor(1,1,0)      # Yellow Color
                    glBegin(GL_QUADS)
                    glVertex(i,j)
                    glVertex(i+50,j)
                    glVertex(i+50,j-50)
                    glVertex(i,j-50)
                    glEnd()
                else:
                    glColor(0,1,1)      # Sky blue Color
                    glBegin(GL_QUADS)
                    glVertex(i,j)
                    glVertex(i+50,j)
                    glVertex(i+50,j-50)
                    glVertex(i,j-50)
                    glEnd()
                clr = clr + 1          # Incrementing the clr variable

    # Drawing Level 2 Ground.
    if Level == 2:
        glLoadIdentity()
        for j in range(150, -150, -50):
            for i in range (-225, 225, 50):
                if(clr % 2 == 1):
                    glColor(1,1,0)      # Yellow Color
                    glBegin(GL_QUADS)
                    glVertex(i, j)
                    glVertex(i+50, j)
                    glVertex(i+50, j-50)
                    glVertex(i, j-50)
                    glEnd()
                else:
                    glColor(0, 1, 1)      # Sky blue Color
                    glBegin(GL_QUADS)
                    glVertex(i, j)
                    glVertex(i+50, j)
                    glVertex(i+50, j-50)
                    glVertex(i, j-50)
                    glEnd()
                clr = clr + 1           # Incrementing the clr variable

    # Drawing Level 3 Ground.
    elif Level == 3:
        glLoadIdentity()

        clr = 0
        for j in range(175, -175, -50):
            for i in range (-175, 175, 50):
                if (j == 175 and (i == -175 or i == 125)) or (j == -125 and (i == -175 or i == 125)):
                    clr = clr + 1
                    continue
                if(clr % 2 == 1):
                    glColor(1, 1, 1)  # White Color
                    glBegin(GL_QUADS)
                    glVertex(i, j)
                    glVertex(i+50, j)
                    glVertex(i+50, j-50)
                    glVertex(i, j-50)
                    glEnd()
                else:
                    glColor(0, 1, 1)  # Sky Blue Color
                    glBegin(GL_QUADS)
                    glVertex(i, j)
                    glVertex(i+50, j)
                    glVertex(i+50, j-50)
                    glVertex(i, j-50)
                    glEnd()
                clr = clr + 1       # Incrementing the clr variable

""" This Function is responsible for drawing the ground Border. """

def DrawPlaygroundBorder():
    glLoadIdentity()
    global Level
    # Level 1 & Level 2 Same Border
    if Level == 1 or Level == 2:
        glColor(0, 0, 0)    # Black Color
        glLineWidth(5)      # Width 5px
        glBegin(GL_LINE_LOOP)
        glVertex(-325, 50, 0)
        glVertex(-225, 50, 0)
        glVertex(-225, 150, 0)
        glVertex(225, 150, 0)
        glVertex(225, 50, 0)
        glVertex(325, 50, 0)
        glVertex(325, -50, 0)
        glVertex(225, -50, 0)
        glVertex(225, -150, 0)
        glVertex(-225, -150, 0)
        glVertex(-225, -50, 0)
        glVertex(-325, -50, 0)
        glVertex(-325, 50, 0)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex(-325, 50)
        glVertex(-325, -50)
        glVertex(-225, -50)
        glVertex(-225, 50)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex2d(225,50)
        glVertex2d(325,50)
        glVertex2d(325,-50)
        glVertex2d(225,-50)
        glEnd()
    # Level 3 Border
    elif Level == 3:
        glLoadIdentity()

        glColor(0, 0, 0)    # Black Color
        glLineWidth(5)      # Width 5px
        glBegin(GL_LINE_LOOP)
        glVertex(-175, 25, 0)
        glVertex(-175, 125, 0)
        glVertex(-125, 125, 0)
        glVertex(-125, 175, 0)
        glVertex(125, 175, 0)
        glVertex(125, 125, 0)
        glVertex(175, 125, 0)
        glVertex(175, 25, 0)
        glVertex(175, -25, 0)
        glVertex(175, -125, 0)
        glVertex(125, -125, 0)
        glVertex(125, -175, 0)
        glVertex(-125, -175, 0)
        glVertex(-125, -125, 0)
        glVertex(-175, -125, 0)
        glVertex(-175, -25, 0)
        glEnd()
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        glVertex(-275, 25)
        glVertex(-275, -25)
        glVertex(-175, -25)
        glVertex(-175, 25)
        glEnd()
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        glVertex(175, 25)
        glVertex(275, 25)
        glVertex(275, -25)
        glVertex(175, -25)
        glEnd()

""" This Function is responsible for Rendering Objects. """

def RenderingObjects():
    glLoadIdentity()
    global Level, visibleSrc

    # rendering images for Level 1
    if Level == 1:
        glTranslate(0, 20, 0)
        glScale(.40, .40, 1)
        imageSrc[1].render()            # Rendering Upper elements for level 1
        glLoadIdentity()
        glTranslate(0, -50, 0)
        glScale(0.4, 0.4, 1)
        imageSrc[2].render()            # Rendering the game logo
        glLoadIdentity()
        glTranslate(600, 25, 0)
        glScale(0.4, 0.4, 1)
        imageSrc[4].render()            # Rendering Yam Char
        glLoadIdentity()
        glTranslate(50, 25, visibleSrc[0])
        glScale(0.05, 0.05, 1)
        imageSrc[5].render()            # Rendering a Candy
        glLoadIdentity()
        glTranslate(150, 125, visibleSrc[1])
        glScale(0.05, 0.05, 1)
        imageSrc[5].render()            # Rendering a Candy
        glLoadIdentity()
        glTranslate(-50, -125, visibleSrc[2])
        glScale(0.05, 0.05, 1)
        imageSrc[5].render()            # Rendering a Candy

    # rendering images for Level 2
    elif Level == 2:

        glLoadIdentity()
        glTranslate(600,25, 0)
        glScale(0.4, 0.4, 1)
        imageSrc[4].render()             # Rendering Yam Char
        glLoadIdentity()
        glTranslate(50, 25, visibleSrc[0])
        glScale(0.05, 0.05, 1)
        imageSrc[5].render()             # Rendering a Candy
        glLoadIdentity()
        glTranslate(150, 125, visibleSrc[1])
        glScale(0.05, 0.05, 1)
        imageSrc[5].render()             # Rendering a Candy
        glLoadIdentity()
        glTranslate(-50, -125, visibleSrc[2])
        glScale(0.05, 0.05, 1)
        imageSrc[5].render()             # Rendering a Candy

    # rendering images for Level 3
    elif Level == 3:
        glLoadIdentity()
        glTranslate(550, 15, 0)
        glScale(0.4, 0.4, 1)
        imageSrc[4].render()            # Rendering Yam Char
        glLoadIdentity()
        glTranslate(-100, 150, visibleSrc[0])
        glScale(0.04, 0.04, 1)
        imageSrc[5].render()            # Rendering a Candy
        glLoadIdentity()
        glTranslate(100, 150, visibleSrc[1])
        glScale(0.04, 0.04, 1)
        imageSrc[5].render()            # Rendering a Candy
        glLoadIdentity()
        glTranslate(-150, 100, visibleSrc[2])
        glScale(0.04, 0.04, 1)
        imageSrc[5].render()            # Rendering a Candy
        glLoadIdentity()
        glTranslate(150, 100, visibleSrc[3])
        glScale(0.04, 0.04, 1)
        imageSrc[5].render()            # Rendering a Candy

""" This Function is responsible for Drawing the text [Scores, Death]. """

def drawText(string, x, y):
    glLineWidth(2)    # Line with 2px
    glColor(0, 0, 0)  # Black Color
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.2, 0.2, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

""" This Function is responsible for Controlling the keyboard events. """

def keyboard(key, x, y):
    global Score, Death, keyboard_x, keyboard_y, visibleSrc, audioSrc, Level, PlaySound, imageSrc

    # Pressing "s" is used to start the game.
    if key == b"s" and Level == 0:
        Level = 1
        visibleSrc[4] = 200

    # Pressing "v" is used to control the sound play
    if key == b"v":
        PlaySound = not PlaySound
        if PlaySound and ( Level == 0 or Level == 1) :
            audioSrc[0].play()
        elif PlaySound and Level == 2:
            audioSrc[4].play()
        elif PlaySound and Level == 3:
            audioSrc[5].play()
        else:
            audioSrc[0].stop()
            audioSrc[1].stop()
            audioSrc[2].stop()
            audioSrc[3].stop()
            audioSrc[4].stop()
            audioSrc[5].stop()

    # Pressing "c" is used to continue playing and moving to next level
    if key == b"c" and Level == 1:
        keyboard_x = -255   # Initial Position for level 1 for mim char
        keyboard_y = 25     # Initial Position for level 1 for mim char
        PlaySound = 2
        audioSrc[0].stop()
        audioSrc[1].stop()
        audioSrc[2].stop()
        audioSrc[3].stop()
        audioSrc[4].play()
        audioSrc[5].stop()
        Level = 2
        Score[1] = Score[0]
        Death[1] = Death[0]
        for j in range(3):
            visibleSrc[j] = 0
    elif key == b"c" and Level == 2:
        keyboard_x = -205   # Initial Position for level 3 for mim char
        keyboard_y = 0      # Initial Position for level 3 for mim char
        PlaySound = 3
        audioSrc[0].stop()
        audioSrc[1].stop()
        audioSrc[2].stop()
        audioSrc[3].stop()
        audioSrc[4].stop()
        audioSrc[5].play()
        Level = 3
        Score[2] = Score[1]
        Death[2] = Death[1]
        for j in range(3):
            visibleSrc[j] = 0

    # Pressing "q" is used to close the game
    if key == b"q":
        sys.exit(0)

    # Pressing "r" is used to reset everything
    if key == b"r":
        if Level == 1:
            Death[0] = 0
            Score[0] = 0
            for j in range(3):
                visibleSrc[j] = 0
            keyboard_x = -255
            keyboard_y = 25
        elif Level == 2:
            Death[1] = Death[0]
            Score[1] = Score[0]
            for j in range(3):
                visibleSrc[j] = 0
            keyboard_x = -255
            keyboard_y = 25
        elif Level == 3:
            Death[2] = Death[1]
            Score[2] = Score[1]
            keyboard_x = -205
            keyboard_y = 0
            for j in range(4):
                visibleSrc[j] = 0


""" This Function is responsible for Controlling the keyboard special arrows and detection of walls. """

def arrow_keys(key, x, y):
    global keyboard_x, keyboard_y, Level

    if key == GLUT_KEY_RIGHT and (Level == 1 or Level == 2) and (keyboard_x < 255 and (keyboard_x < 195 or (keyboard_y <= 25 and keyboard_y >= -25) )): #right arrow key is pressed
        keyboard_x += 50
    elif key == GLUT_KEY_LEFT and (Level == 1 or Level == 2) and (keyboard_x > -305 and( keyboard_x > -205 or (keyboard_y <= 25 and keyboard_y >= -25) )): #left arrow key is pressed
        keyboard_x -= 50
    elif key == GLUT_KEY_UP and (Level == 1 or Level == 2) and (keyboard_y < 25 or (keyboard_x > -255 and keyboard_x < 205) and keyboard_y < 125 ):        # Up arrow key is pressed
        keyboard_y += 50
    elif key == GLUT_KEY_DOWN and (Level == 1 or Level == 2) and  (keyboard_y > -25 or (keyboard_x > -255 and keyboard_x< 205) and keyboard_y > -125):        # Down arrow key is pressed
        keyboard_y -= 50

    if key == GLUT_KEY_RIGHT and Level == 3 and (keyboard_x < 55 or (keyboard_y < 150 and keyboard_y > -150))and (keyboard_x < 105 or keyboard_y == 0) and keyboard_x < 205:
        keyboard_x += 50
    elif key == GLUT_KEY_LEFT and Level == 3 and (keyboard_x > -105 or (keyboard_y < 150 and keyboard_y > -150))and (keyboard_x > -155 or keyboard_y == 0)and keyboard_x > -255:
        keyboard_x -= 50
    elif key == GLUT_KEY_UP and Level == 3 and (keyboard_y < 0 or (keyboard_x > -205 and keyboard_x < 155)) and (keyboard_y < 100 or (keyboard_x > -155 and keyboard_x < 105))and keyboard_y < 150 :
        keyboard_y += 50
    elif key == GLUT_KEY_DOWN and Level == 3 and (keyboard_y > 0 or (keyboard_x > -205 and keyboard_x < 155)) and (keyboard_y > -100 or (keyboard_x > -155 and keyboard_x < 105))and keyboard_y > -150 :
        keyboard_y -= 50

""" This is our display function. """

def Display():

    global imageSrc, visibleSrc
    global left, up, down, keyboard_x, keyboard_y, dix, diy1, diy2, Score, Death, x, y, Level, xo, yo, xn, yn

    for i in range (0,1000):
        print(0)

    glClear(GL_COLOR_BUFFER_BIT )
    glLoadIdentity()
    glTranslate(0, 0, visibleSrc[4])
    glScale(.42, .42, 1)
    imageSrc[0].render()

    if Level == 1:
        DrawGround()
        DrawStart_End()
        DrawPlaygroundBorder()
        string = str(Score[0])
        drawText(string, -155, 240)
        string = str(Death[0])
        drawText(string, -160, 170)

        # Drawing spheres.
        for i in range(0, 4):
            glColor(1, 0, 0)
            glLoadIdentity()
            glTranslate(left, Spheres[i], 0)
            glutSolidSphere(15, 50, 50)

        left = left - dix       # Decreasing the left to do the animation by translating spheres to left
        # Collision between spheres and character.
        if(keyboard_x+10 >= left-15 and keyboard_x-10 <= left+15 and (keyboard_y <= 25 and keyboard_y >= -25 or keyboard_y == 125 or keyboard_y == -125)):
            keyboard_x = -255
            keyboard_y = 25
            Death[0] += 1
            Score[0] = 0
            visibleSrc[0] = 0
            visibleSrc[1] = 0
            visibleSrc[2] = 0
            audioSrc[2].play()

        # Collision between spheres and walls.
        if(left <= -215 or left >= 215):
            dix = - dix     # Change the direction of movement after the collision with wall.

        # Rendering Mim Char
        glLoadIdentity()
        glTranslate(keyboard_x, keyboard_y, 0)
        glTranslate(335, 20, 0)
        glScale(.4, .4, 1)
        imageSrc[3].render()

        RenderingObjects()

        # Collision between candies and character.

        if(keyboard_x >= 25 and keyboard_x <= 75 and keyboard_y >= 0 and keyboard_y <= 50 and visibleSrc[0] == 0):
            visibleSrc[0] = 200
            Score[0] += 100
            audioSrc[1].play()
        if(keyboard_x >= 125 and keyboard_x <= 175 and keyboard_y >= 100 and keyboard_y <= 150 and visibleSrc[1] == 0):
            visibleSrc[1] = 200
            Score[0] += 100
            audioSrc[1].play()
        if(keyboard_x >= -75 and keyboard_x <= -25 and keyboard_y >= -150 and keyboard_y <= -100 and visibleSrc[2] == 0):
            visibleSrc[2] = 200
            Score[0] += 100
            audioSrc[1].play()

        # Winning the game.
        if(keyboard_x >= 200 and Score[0] == 300):
            glLoadIdentity()
            glTranslate(0, 0, 0)
            glScale(0.42, 0.42, 1)
            imageSrc[6].render()
            audioSrc[3].play()

    elif Level == 2:
        glLoadIdentity()
        glTranslate(0, 0, 0)
        glScale(0.42, 0.42, 1)
        imageSrc[7].render()


        DrawGround()
        DrawStart_End()
        DrawPlaygroundBorder()
        string = str(Score[1])
        drawText(string, -155, 240)
        string = str(Death[1])
        drawText(string, -160, 170)

        # Drawing up spheres.

        for i in range(0, 5):
            glColor(1, 0, 0)
            glLoadIdentity()
            glTranslate(Spheres2[i], up, 0)
            glutSolidSphere(15, 50, 50)

        # Drawing down spheres.

        for i in range(0, 4):
            glColor(1, 0, 0)
            glLoadIdentity()
            glTranslate(Spheres2[i+5], down, 0)
            glutSolidSphere(15, 50, 50)

        up = up - diy1      # Decreasing the up initial value for animation by translating spheres into new up
        down = down + diy2  # Increasing the down initial value for animation by translating spheres into new down


        # Collision between spheres and character.

        if(keyboard_y+10 >= up-15 and keyboard_y-10 <= up+15 and (keyboard_x == -205 or keyboard_x == -105 or keyboard_x == -5 or keyboard_x == 95 or keyboard_x == 195)):
            keyboard_x = -255
            keyboard_y = 25
            Death[1] += 1
            Score[1] = Score[0]
            visibleSrc[0] = 0
            visibleSrc[1] = 0
            visibleSrc[2] = 0
            audioSrc[2].play()

        if(keyboard_y+10 >= down-15 and keyboard_y-10 <= down+15 and (keyboard_x == -155 or keyboard_x == -55 or keyboard_x == 45 or keyboard_x == 145 )):
            keyboard_x = -255
            keyboard_y = 25
            Death[1] += 1
            Score[1] = Score[0]
            visibleSrc[0] = 0
            visibleSrc[1] = 0
            visibleSrc[2] = 0
            audioSrc[2].play()

        # Collision between spheres and walls.

        if(up <= -135 or up >= 135):
            diy1 = - diy1       # Changing the direction of up spheres after collision with wall
        if(down <= -135 or down >= 135):
            diy2 = - diy2       # Changing the direction of down spheres after collision with wall


        # Collision between candies and character.

        if(keyboard_x >= 25 and keyboard_x <= 75 and keyboard_y >= 0 and keyboard_y <= 50 and visibleSrc[0] == 0):
            visibleSrc[0] = 200
            Score[1] += 100
            audioSrc[1].play()
        if(keyboard_x >= 125 and keyboard_x <= 175 and keyboard_y >= 100 and keyboard_y <= 150 and visibleSrc[1] == 0):
            visibleSrc[1] = 200
            Score[1] += 100
            audioSrc[1].play()
        if(keyboard_x >= -75 and keyboard_x <= -25 and keyboard_y >= -150 and keyboard_y <= -100 and visibleSrc[2] == 0):
            visibleSrc[2] = 200
            Score[1] += 100
            audioSrc[1].play()

        # Rendering Mim Character.

        glLoadIdentity()
        glTranslate(keyboard_x, keyboard_y, 0)
        glTranslate(335, 20, 0)
        glScale(.4, .4, 1)
        imageSrc[3].render()

        RenderingObjects()

        # Winning the game.

        if(keyboard_x >= 200 and Score[1] == 600):
            glLoadIdentity()
            glTranslate(0, 0, 0)
            glScale(0.42, 0.42, 1)
            imageSrc[8].render()
            audioSrc[3].play()

    elif Level == 3:

        # Rendering Level 3 Background.

        glLoadIdentity()
        glTranslate(0, 0, 0)
        glScale(0.42, 0.42, 1)
        imageSrc[9].render()

        DrawGround()
        DrawPlaygroundBorder()
        DrawStart_End()
        string = str(Score[2])
        drawText(string, -155, 240)
        string = str(Death[2])
        drawText(string, -160, 170)

        # Rotating Equations ...

        for i in range(0, 12, 1):
            xn = xo[i] * cos(angle) - yo[i] * sin(angle)
            yn = xo[i] * sin(angle) + yo[i] * cos(angle)
            xo[i] = xn
            yo[i] = yn

        # Collision between spheres and character.

        for i in range (0,12,1):
            if(keyboard_x == -5 and keyboard_y == 0):
                keyboard_x = -205
                keyboard_y = 0
                Death[2] += 1
                Score[2] = Score[1]
                audioSrc[2].play()
                for j in range(4):
                    visibleSrc[j] = 0
            elif (keyboard_x+15 >= xo[i]-15 and keyboard_x+15 <= xo[i]+15 and keyboard_y-15 >= yo[i]-15 and keyboard_y-15 <= yo[i]+15):
                keyboard_x = -205
                keyboard_y = 0
                Death[2] += 1
                Score[2] = Score[1]
                audioSrc[2].play()
                for j in range (4):
                    visibleSrc[j] = 0
            elif (keyboard_x+15 >= -xo[i]-15 and keyboard_x+15 <= -xo[i]+15 and keyboard_y+15 >= -yo[i]-15 and keyboard_y+15 <= -yo[i]+15):
                keyboard_x = -205
                keyboard_y = 0
                Death[2] += 1
                Score[2] = Score[1]
                audioSrc[2].play()
                for j in range (4):
                    visibleSrc[j] = 0
            elif (keyboard_x-15 >= xo[i]-15 and keyboard_x-15 <= xo[i]+15 and keyboard_y+15 >= yo[i]-15 and keyboard_y+15 <= yo[i]+15):
                keyboard_x = -205
                keyboard_y = 0
                Death[2] += 1
                Score[2] = Score[1]
                audioSrc[2].play()
                for j in range (4):
                    visibleSrc[j] = 0
            elif (keyboard_x-15 >= -xo[i]-15 and keyboard_x-15 <= -xo[i]+15 and keyboard_y-15 >= -yo[i]-15 and keyboard_y-15 <= -yo[i]+15):
                keyboard_x = -205
                keyboard_y = 0
                Death[2] += 1
                Score[2] = Score[1]
                audioSrc[2].play()
                for j in range (4):
                    visibleSrc[j] = 0

        # Drawing spheres in their position after rotating ..

        glColor(1,0,0)
        glLoadIdentity()
        glutSolidSphere(15, 50, 50)
        for i in range(0,12):
            glLoadIdentity()
            glTranslate(xo[i], yo[i], 0)
            glutSolidSphere(15, 50, 50)

        # Rendering Mim Character

        glLoadIdentity()
        glTranslate(keyboard_x, keyboard_y, 0)
        glTranslate(335, 20, 0)
        glScale(.4, .4, 1)
        imageSrc[3].render()

        RenderingObjects()

        # Collision between candies and character.

        if(keyboard_x >= -125 and keyboard_x <= -75 and keyboard_y >= 125 and keyboard_y <= 175 and visibleSrc[0] == 0):
            visibleSrc[0] = 200
            Score[2] += 100
            audioSrc[1].play()
        if(keyboard_x >= 75 and keyboard_x <= 125 and keyboard_y >= 125 and keyboard_y <= 175 and visibleSrc[1] == 0):
            visibleSrc[1] = 200
            Score[2] += 100
            audioSrc[1].play()
        if(keyboard_x >= -175 and keyboard_x <= -125 and keyboard_y >= 75 and keyboard_y <= 125 and visibleSrc[2] == 0):
            visibleSrc[2] = 200
            Score[2] += 100
            audioSrc[1].play()
        if(keyboard_x >= 125 and keyboard_x <= 175 and keyboard_y >= 75 and keyboard_y <= 125 and visibleSrc[3] == 0):
            visibleSrc[3] = 200
            Score[2] += 100
            audioSrc[1].play()

        # Winning the game

        if(keyboard_x >= 175 and Score[2] == 1000):
            glLoadIdentity()
            glTranslate(0, 0, 0)
            glScale(0.42, 0.42, 1)
            imageSrc[10].render()
            audioSrc[3].play()


    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Mim&Yam Game");
    glutIdleFunc(Display)
    glutDisplayFunc(Display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(arrow_keys)
    init()
    glutMainLoop()


main()
